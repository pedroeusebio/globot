import secrets
from flask import Flask, request
from bot import Bot
from conversation import TextResponse
from repo import ConversationRepository

conversation_repository = ConversationRepository()

app = Flask(__name__)

VERIFY_TOKEN = "globotftw"
bot = Bot(secrets.ACCESS_TOKEN)

"""
@app.route("/polls", methods=['GET', 'POST'])
def polls():
    if request.method == 'GET':
        poll_repo.get_all()
    if request.method == 'POST':
        # UC Create Poll
        poll = Poll(argslalalamsdka)
        poll_repo.save(poll)

        buttons = map(lambda q: , poll.answers)

        # send poll to assigned members
        convs = conversation_repo.all()
        all_users = map(lambda c: c.user, convs)
        users = filter(lambda u: poll.is_for(u), convs)

        for user in users:
            bot.send_button_message(user.recipient_id, poll.text, )
"""

def get_conversations_for(team_slug):
    ret = []

    for recipient_id, conversation in conversation_repository.conversations:
        if conversation.user.team_slug == team_slug:
            ret.append(conversation)

    return ret

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

@app.route("/sendRealTimeMessage/", methods=['POST'])
def sendReaTimeMessage():
    if request.method == 'POST':
        mandante =  request.args.get('mandante')
        visitante = request.args.get('visitante')
        msg = request.args.post('msg')

        convs_mandante  = get_conversations_for(mandante)
        convs_visitante = get_conversations_for(visitante)

        convs = []

        if len(convs_mandante) > 1:
            convs += convs_mandante

        if len(convs_visitante) > 1:
            convs += convs_visitante

        for conv in convs:
            bot.send_text_message(msg)

        return "Success"

if __name__ == "__main__":
    app.run(host="127.0.0.1")
