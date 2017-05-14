class Poll:
    def __init__(self, question, possible_answers, uid=None):
        self.uid = uid
        self.question = question
        self.possible_answers = possible_answers
        self.answers = {}

    def add_answer(self, recipient_id, answer):
        if self.answers.get(recipient_id) != None:
            raise Exception("Recipient already answered")

        if answer not in self.possible_answers:
            raise Exception("Invalid answer")

        self.answers[recipient_id] = answer

    def results(self):
        # Map reduce boladão
        pass
