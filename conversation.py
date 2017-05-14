# -*- coding: utf-8 -*-
from pprint import pprint 

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

Match = namedtuple('Match', 'mandante visitante')

class Subscriptions:
    def __init__(self):
        self.pending = None
        self.subbed = set()

    def add(self, k):
        self.pending = k

    def confirm(self):
        self.subbed.add(self.pending)
        self.pending = None

    def cancel(self):
        self.pending = None

    def has(self, k):
        return k in self.subbed

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
        self.realtime_subs = Subscriptions()
        self.interest_subs = Subscriptions()
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

        if self.state == State.YESNO_REALTIME:
            return self.yesno_realtime(msg)

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
            self.interest_subs.confirm()
            return TextResponse("Ok! Irei te avisar quando for a hora 😉")
        else:
            self.interest_subs.cancel()

    def yesno_realtime(self, msg):
        self.state = State.PROCESSING
        if is_positive(msg):
            self.realtime_subs.confirm()
            return TextResponse("Ok! Você irá receber o jogo em tempo real. 😉")
        else:
            self.realtime_subs.cancel()

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
                return (team_slug, programacao.get_last_game_formatted(team_id, ))
        return None

    def getGameData(self, msg):
        maxlen = len(msg)
        prev_ind = self.find_token_index(msg, ["ultimo", "último", "anterior", "passada"])
        game_ind = self.find_token_index(msg, ["jogo", "partida", "game", "rodada"])
        team_ind = self.find_token_index(msg, utils.get_list_of_equipes_popular_names())
        date_limit = strftime("%Y-%m-%dT%H:%M:%S", gmtime())
        upcoming = True

        if (game_ind == maxlen):
            return None

        if (prev_ind != maxlen):
            upcoming = False

        team_slug = ""
        if (team_ind != maxlen):
            team_slug = self.get_token_on_ind(team_ind, msg).lower()
        else:
            team_slug = self.user.team_slug

        team_id = utils.get_equipe_id_by_slug(team_slug)

        if upcoming:
            game_info, ref = programacao.get_next_game(team_id, date_limit)
            pprint(team_slug)
            pprint(team_id)
            pprint(game_info)
            pprint(ref)
        else:
            game_info, ref = programacao.get_last_game(team_id, date_limit)

        if game_info is None:
            return upcoming, None, None

        return upcoming, game_info, ref

    def default(self, msg):
        return TextResponse("Não sei o que dizer HAHAHA. Só vamos, {}! ⚽".format(self.user.team_popular_name))

    def notify_game(self, match):
        mandante, visitante = match
        msg = "Jogo %s x %s começando em 1 hora.\nDeseja receber notificações em tempo real?" % (mandante, visitante)
        self.realtime_subs.add(match)
        self.state = State.YESNO_REALTIME
        return YesNoResponse(msg)

    def process_request(self, msg):
        game_data = self.getGameData(msg)
        if game_data is not None:
            upcoming, game_info, ref = game_data
            if game_info is None:
                return TextResponse("Não foi encontrado um jogo {}.".format("futuro" if upcoming else "passado"))

            game_msg = programacao.format_game(upcoming, game_info, ref)

            if upcoming:
                msg = game_msg + "\nDeseja ser notificado 1 hora antes do início do jogo?"

                self.state = State.YESNO_NOTIFY
                mandante_id = game_info['equipe_mandante_id']
                mandante_slug = utils.get_slug_by_equipe_id(mandante_id)
                visitante_id = game_info['equipe_visitante_id']
                visitante_slug = utils.get_slug_by_equipe_id(visitante_id)
                match = Match(mandante_slug, visitante_slug)
                self.interest_subs.add(match)
                pprint(self.interest_subs.__dict__)

                return YesNoResponse(msg)
            else:
                return TextResponse(game_msg)

        return self.default(msg)
