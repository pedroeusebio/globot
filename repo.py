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
