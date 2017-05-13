from collections import namedtuple
from user import User
from fuzzywuzzy import fuzz
import programacao
import utils
from time import gmtime, strftime

TextResponse = namedtuple('TextResponse', 'text')

class State:
    ONBOARDING = 1
    ASKING_TEAM = 2
    CONFIRMING_TEAM = 3
    PROCESSING = 4

class Conversation:
    def __init__(self, recipient_id):
        self.user = User(recipient_id)
        self.state = State.ONBOARDING
        self.messages = []

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

        return self.default(msg)

    def onboarding(self, msg):
        self.state = State.ASKING_TEAM
        return TextResponse("Ola, {}. Vamos começar. Qual seu time do coração?".format(self.user.name))

    def asking_team(self, msg):
        # TODO : Use api
        self.user.team_slug = msg
        self.state = State.CONFIRMING_TEAM
        return TextResponse("Irado! Seu time é o {}, certo?".format(self.user.team_slug))

    def confirming_team(self, msg):
        if fuzz.ratio(msg, 'sim') > 49:
            self.state = State.PROCESSING
            return TextResponse("Show! Então é isso.")

        return self.onboarding(msg)
    
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

    def process_request(self, msg):
        next_ind = self.find_token_index(msg, ["proximo", "próximo"])
        game_ind = self.find_token_index(msg, ["jogo", "partida", "game", "rodada"])
        team_ind = self.find_token_index(msg, utils.get_list_of_equipes_popular_names())
        if (next_ind != -1 and game_ind != -1 and team_ind != -1):
            if (next_ind < game_ind and game_ind < team_ind):
                team_slug = self.get_token_on_ind(team_ind, msg)
                return TextResponse(programacao.get_next_game_formatted(utils.get_equipe_id_by_slug(team_slug), strftime("%Y-%m-%d", gmtime())))
        self.default(msg)
                
    def default(self, msg):
        return TextResponse("Não sei o que dizer HAHAHA. Só vamo {}!".format(self.user.team_slug))
