# -*- coding: utf-8 -*-

import database
from collections import namedtuple
from user import User
from fuzzywuzzy import fuzz
import programacao
import random
import utils
from time import gmtime, strftime

TextResponse = namedtuple('TextResponse', 'text')
ImageUrlResponse = namedtuple('ImageUrlResponse', 'url')
YesNoResponse = namedtuple('YesNoResponse', 'text')


class State:
    ONBOARDING = 1
    ASKING_TEAM = 2
    CONFIRMING_TEAM = 3
    PROCESSING = 4
    YESNO_NOTIFY = 5
    YESNO_REALTIME = 6


yes_array = ['sim', 'yes', 'yeah', 'si', 'claro', 'isso', 'eh', 'aham', 'perfeito', 'blz', 'jaeh']
def is_positive(msg):
    for yess in yes_array:
        if yess.lower() == msg.lower():
            return True
    return False

class Conversation:

    def __init__(self, recipient_id):
        self.user = User(recipient_id)
        self.state = State.ONBOARDING
        self.messages = []
        database.Conversations[recipient_id] = self
        database.Users[recipient_id] = self.user

    def message(self, msg):
        self.messages.append(msg)

        if self.state == State.ONBOARDING:
            return self.onboarding(msg)

        if self.state == State.ASKING_TEAM:
            return self.asking_team(msg)

        if self.state == State.CONFIRMING_TEAM:
            return self.confirming_team(msg)

        if self.state == State.PROCESSING:
            return self.process_request(msg)

        if self.state == State.YESNO_NOTIFY:
            return self.yesno_notify(msg)

        return self.default(msg)

    def onboarding(self, msg):
        self.state = State.ASKING_TEAM
        return TextResponse("Alô alô, vamos nessa, {}! ⚽ \nQual é o seu time do coração? <3".format(self.user.name))

    def asking_team(self, msg):
        equipes = utils.get_list_of_equipes_popular_names() # String: 'Flamengo'
        for equipe in equipes:
            if fuzz.ratio(equipe, msg) > 49:
                self.user.team_slug = msg.lower().replace(" ", "-")
                self.user.team_popular_name = utils.get_popular_name_by_slug(self.user.team_slug)
                self.user.team_id = utils.get_equipe_id_by_slug(self.user.team_slug)
                if self.user.team_id is None:
                    break
                self.state = State.CONFIRMING_TEAM
                return TextResponse("Irado! 😎 Seu time é o {}, né?".format(self.user.team_popular_name))
        return TextResponse('Você entrou com um time inválido! Por favor, tente novamente.')

    def confirming_team(self, msg):
        if is_positive(msg):
            self.state = State.PROCESSING
            return [TextResponse("Show! Vamos torcer juntos para o {}!!".format(utils.get_nickname_from_slug(self.user.team_slug))), ImageUrlResponse(utils.get_equipe_escudo_url_by_id(self.user.team_id))]
        self.state = State.ASKING_TEAM
        return TextResponse('Por favor, tente novamente. Qual o seu time do coração? <3')

    def yesno_notify(self, msg):
        self.state = State.PROCESSING
        if is_positive(msg):
            return TextResponse("Ok! Irei te avisar quando for a hora 😉")
        else:
            self.user.interest = None

    def get_min_index_from_arr(self, arr, msg):
        index = len(msg)
        for x in  arr:
            cur_ind = msg.find(x.lower())
            if cur_ind != -1:
                index = min(index, cur_ind)
        return index

    def find_token_index(self, msg, arr):
        msg = msg.lower()
        return self.get_min_index_from_arr(arr, msg)

    def get_token_on_ind(self, ind, msg):
        for i in range(ind, len(msg)):
            if (not msg[i].isalpha()):
                return msg[ind:i]
        return msg[ind:]


    def isNextGameRequest(self, msg):
        next_ind = self.find_token_index(msg, ["proximo", "próximo", "proxima", "próxima"])
        game_ind = self.find_token_index(msg, ["jogo", "partida", "game", "rodada"])
        team_ind = self.find_token_index(msg, utils.get_list_of_equipes_popular_names())
        maxlen = len(msg)
        if (next_ind != maxlen and game_ind != maxlen):
            team_slug = ""
            if (team_ind != maxlen):
                team_slug = self.get_token_on_ind(team_ind, msg).lower()
            else:
                team_slug = self.user.team_slug

            team_id = utils.get_equipe_id_by_slug(team_slug)
            if (team_id is not None):
                return (team_slug, programacao.get_next_game_formatted(team_id, strftime("%Y-%m-%dT%H:%M:%S", gmtime())))
        return None

    def isLastGameRequest(self, msg):
        next_ind = self.find_token_index(msg, ["ultimo", "último", "anterior", "passada"])
        game_ind = self.find_token_index(msg, ["jogo", "partida", "game", "rodada"])
        team_ind = self.find_token_index(msg, utils.get_list_of_equipes_popular_names())
        maxlen = len(msg)
        if (next_ind != maxlen and game_ind != maxlen):
            team_slug = ""
            if (team_ind != maxlen):
                team_slug = self.get_token_on_ind(team_ind, msg).lower()
            else:
                team_slug = self.user.team_slug

            team_id = utils.get_equipe_id_by_slug(team_slug)
            if (team_id is not None):
                return (team_slug, programacao.get_last_game_formatted(team_id, strftime("%Y-%m-%dT%H:%M:%S", gmtime())))
        return None

    def default(self, msg):
        return TextResponse("Não sei o que dizer HAHAHA. Só vamos, {}! ⚽".format(self.user.team_popular_name))

    def notify_game(self, mandante, visitante):
        msg = "Jogo %s x %s começando em 1 hora.\nDeseja receber notificações em tempo real?" % (mandante, visitante)
        self.state = State.YESNO_REALTIME
        return YesNoResponse(msg)

    def process_request(self, msg):
        game_data = self.isNextGameRequest(msg)
        if game_data is not None:
            team_slug, msg = game_data
            if (msg == "Não foram encontrado jogos futuros."):
                return TextResponse(msg)

            else:
                msg += "\nDeseja ser notificado 1 hora antes do início do jogo?"

                self.state = State.YESNO_NOTIFY
                self.user.interest = team_slug

                return YesNoResponse(msg)

        game_data = self.isLastGameRequest(msg)
        if game_data is not None:
            team_slug, resp = game_data
            return TextResponse(resp)

        return self.default(msg)
