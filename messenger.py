from flask import Flask, request
from pymessenger.bot import Bot
from repositorio_conversa import ConversationRepository, TextResponse

conversation_repository = ConversationRepository()

app = Flask(__name__)

ACCESS_TOKEN = "EAAUiQJbwNboBABscA7dPr6dtBll5yTwo4TZCybdV89aVBNXbAFMJFVKbcwcRef4WdIa261AYIakYYZArZAiXRsFcCCmqvDm9dVWh8e2ytgz1dC6BRwyXxAyOY8apXPNeTb7HhzoTjwAwxoxzfEs4nzr9HD2tTwtbZBxh0DveUQZDZD"
VERIFY_TOKEN = "globotftw"
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    conversation = conversation_repository.get_or_create(recipient_id)
                    if x['message'].get('text'):
                        message = x['message']['text']
                        response = conversation.message(message)
                        if isinstance(response, TextResponse):
                            bot.send_text_message(recipient_id, response.text)
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
