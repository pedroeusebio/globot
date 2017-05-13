from collections import namedtuple
from core.user import User
from fuzzywuzzy import fuzz

TextResponse = namedtuple('TextResponse', 'text')

class State:
    INIT = 0
    ONBOARDING = 1
    ASKING_TEAM = 2
    CONFIRMING_TEAM = 3

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
            self.state = State.INIT
            return TextResponse("Show! Então é isso.")

        return self.onboarding(msg)

    def default(self, msg):
        return TextResponse("Não sei o que dizer HAHAHA. Só vamo {}!".format(self.user.team_slug))
