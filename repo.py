from conversation import Conversation

class ConversationRepository:
    def __init__(self):
        self.conversations = {}

    def get_or_create(self, recipient_id):
        conversation = self.conversations.get(recipient_id)
        if conversation:
            return conversation

        conversation = Conversation(recipient_id)
        self.conversations[recipient_id] = conversation
        return conversation

class PollRepository:
    def __init__(self):
        self.polls = []

    def create(self, poll):
        self.polls.append(poll)
        poll.uid = len(self.polls)
        return poll

    def get_all(self):
        return self.polls

    def get(self, uid):
        if len(self.polls) < uid:
            return None

        return self.polls[uid]
