import secrets
import json
from flask import Flask, request, jsonify, send_from_directory
from pymessenger import Bot
from conversation import TextResponse,ImageUrlResponse, YesNoResponse, Match
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
                    payload = x['postback']['payload']
                    try:
                        payload = json.loads(payload)
                        if payload['type'] == 'poll_answer':
                            answer_poll(recipient_id, payload['uid'], payload['option'])
                        elif payload['type'] == 'as_message' :
                            onmessage(recipient_id, payload['message'])
                    except:
                        from pprint import pprint
                        pprint(x)
                        pprint(payload)
                        if payload == 'setup':
                            onmessage(recipient_id, "ola")

                if 'message' in x:
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        onmessage(recipient_id, message)

                else:
                    pass
        return "Success"

def onmessage(recipient_id, message):
    conversation = conversation_repository.get_or_create(recipient_id)
    responses = conversation.message(message)

    send_response(recipient_id, responses)

def send_response(recipient_id, responses):
    if not isinstance(responses, list):
        responses = [responses]

    for response in responses:
        if isinstance(response, TextResponse):
            bot.send_text_message(recipient_id, response.text)
        elif isinstance(response, ImageUrlResponse):
            bot.send_image_url(recipient_id, response.url)
        elif isinstance(response, YesNoResponse):
            def mkbutton(o):
                return make_button(o, {'type': 'as_message', 'message': o})
            buttons = [mkbutton(o) for o in ['Sim', 'Não']]
            bot.send_button_message(recipient_id, response.text, buttons)

def answer_poll(recipient_id, poll_uid, option):
    poll = poll_repository.get(poll_uid)
    if poll == None:
        return

    poll.add_answer(recipient_id, option)

def make_button(title, payload):
    return {
        "type": "postback",
        "title": title,
        "payload": json.dumps(payload)
    }

@app.route("/createPoll/", methods=['POST'])
def createPoll():
    args = request.get_json()
    team = args.get('team')
    question = args.get('question')
    options = args.get('options')

    poll = Poll(question, options, TeamSlugFilter(team))
    poll_repository.insert(poll)

    def mkbutton(o):
        payload = {
            'type': 'poll_answer',
            'uid': poll.uid,
            'option': o
        }
        return make_button(o, payload)

    convs = conversation_repository.get_by_team(team)
    for conv in convs:
        bot.send_button_message(conv.user.recipient_id, question, [mkbutton(o) for o in options])

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

    match = Match(mandante, visitante)
    convs  = conversation_repository.get_by_realtime(match)

    for conv in convs:
        bot.send_text_message(conv.user.recipient_id, msg)
        if img:
            bot.send_image_url(conv.user.recipient_id, img)

    return "Success"

@app.route("/notifyGame/", methods=['POST'])
def notifyGame():
    args = request.get_json()
    mandante =  args.get('mandante')
    visitante = args.get('visitante')
    match = Match(mandante, visitante)

    convs  = conversation_repository.get_by_interest(match)

    for conv in convs:
        responses = conv.notify_game(match)
        send_response(conv.user.recipient_id, responses)

    return "Success"

@app.route("/admin/<path:path>")
def admin(path):
    return send_from_directory('poll_ui', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
