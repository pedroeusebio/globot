# -*- coding: utf-8 -*-
from collections import namedtuple

TextResponse = namedtuple('TextResponse', 'text')

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

class Conversation:
    def __init__(self, recipient_id):
        self.recipient_id = recipient_id
        self.messages = []

    def message(self, msg):
        self.messages.append(msg)
        return TextResponse("Você disse: {}. Esta é sua {} mensagem.".format(
            msg,
            len(self.messages)
        ))
