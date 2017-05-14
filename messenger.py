import secrets
import json
from flask import Flask, request, jsonify, send_from_directory
from pymessenger import Bot
from conversation import TextResponse,ImageUrlResponse
from repo import ConversationRepository, PollRepository
from poll import Poll
from user import TeamSlugFilter

conversation_repository = ConversationRepository()
poll_repository = PollRepository()

app = Flask(__name__)

VERIFY_TOKEN = "globotftw"
bot = Bot(secrets.ACCESS_TOKEN)

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
                if 'postback' in x:
                    recipient_id = x['sender']['id']
                    conversation = conversation_repository.get_or_create(recipient_id)
                    payload = json.loads(x['postback']['payload'])
                    if payload['type'] == 'poll_answer':
                        answer_poll(recipient_id, payload['uid'], payload['option'])

                if 'message' in x:
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

def answer_poll(recipient_id, poll_uid, option):
    poll = poll_repository.get(poll_uid)
    if poll == None:
        return

    poll.add_answer(recipient_id, option)

@app.route("/createPoll/", methods=['POST'])
def createPoll():
    args = request.get_json()
    team = args.get('team')
    question = args.get('question')
    options = args.get('options')

    poll = Poll(question, options, TeamSlugFilter(team))
    poll_repository.insert(poll)

    def make_button(o):
        payload = {
            'type': 'poll_answer',
            'uid': poll.uid,
            'option': o
        }
        return {
            "type": "postback",
            "title": o,
            "payload": json.dumps(payload)
        }

    convs = conversation_repository.get_by_team(team)
    for conv in convs:
        bot.send_button_message(conv.user.recipient_id, question, [make_button(o) for o in options])

    return "Success"

def poll_to_dict(poll):
    return {
        'question' : poll.question,
        'options' : poll.options,
        'results' : poll.results()
    }

@app.route("/polls", methods=['GET'])
def getPolls():
    return jsonify([poll_to_dict(p) for p in poll_repository.get_all()])

@app.route("/sendRealTimeMessage/", methods=['POST'])
def sendReaTimeMessage():
    args = request.get_json()
    mandante =  args.get('mandante')
    visitante = args.get('visitante')
    msg = args.get('msg')
    img = args.get('img')

    convs_mandante  = conversation_repository.get_by_team(mandante)
    convs_visitante  = conversation_repository.get_by_team(visitante)

    convs = convs_mandante + convs_visitante

    for conv in convs:
        bot.send_text_message(conv.user.recipient_id, msg)
        if img:
            bot.send_image_url(conv.user.recipient_id, img)

    return "Success"

@app.route("/admin/<path:path>")
def admin(path):
    return send_from_directory('poll_ui', path)

if __name__ == "__main__":
    app.run(host="127.0.0.1")
