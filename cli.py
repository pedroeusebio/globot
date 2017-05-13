from conversation import TextResponse
from repo import ConversationRepository

fake_id = 1234
conversation_repository = ConversationRepository()
conversation = conversation_repository.get_or_create(fake_id)

while True:
    message = input('> ')
    response = conversation.message(message)
    if isinstance(response, TextResponse):
        print(response.text)
