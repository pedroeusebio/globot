import secrets

from flask import Flask, request
from pymessenger import Bot
from conversation import TextResponse,ImageUrlResponse
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

                        responses = conversation.message(message)

                        if not isinstance(responses, list):
                            responses = [responses]

                        for response in responses:
                            if isinstance(response, TextResponse):
                                bot.send_text_message(recipient_id, response.text)
                            elif isinstance(response, ImageUrlResponse):
                                bot.send_image_url(recipient_id, response.url)
                else:
                    pass
        return "Success"


@app.route("/createPoll/", methods=['POST'])
def createPoll():
    if request.method == 'POST':
        question = request.args.get('question')
        options = request.args.get('question')
        team = request.args.get('team')

        convs  = get_conversations_for(team)
        for recipient_id, conv in convs:
            bot.send_text_message(recipient_id, t )


@app.route("/sendRealTimeMessage/", methods=['POST'])
def sendReaTimeMessage():
    if request.method == 'POST':
        args = request.get_json()
        mandante =  args.get('mandante')
        visitante = args.get('visitante')
        msg = args.get('msg')

        convs_mandante  = conversation_repository.get_by_team(mandante)
        convs_visitante  = conversation_repository.get_by_team(visitante)

        convs = convs_mandante + convs_visitante

        from pprint import pprint
        pprint(convs)

        for conv in convs:
            bot.send_text_message(conv.user.recipient_id, msg)

        return "Success"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
