from conversation import TextResponse,ImageUrlResponse
from repo import ConversationRepository

fake_id = 1234
conversation_repository = ConversationRepository()
conversation = conversation_repository.get_or_create(fake_id)

while True:
    message = input('> ')
    responses = conversation.message(message)

    if not isinstance(responses, list):
        responses = [responses]

    for response in responses:
        if isinstance(response, TextResponse):
            print(response.text)
        elif isinstance(response, ImageUrlResponse):
            print(response.url)
