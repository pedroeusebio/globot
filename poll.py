class Poll:
    def __init__(self, question, options, filters, uid=None):
        self.uid = uid
        self.question = question
        self.options = options
        self.filters = filters
        self.answers = {}

    def add_answer(self, recipient_id, answer):
        if self.answers.get(recipient_id) != None:
            raise Exception("Recipient already answered")

        if answer not in self.options:
            raise Exception("Invalid answer")

        self.answers[recipient_id] = answer

    def results(self):
        results = {}
        for opt in self.options:
            results[opt] = 0

        for a in self.answers.values():
            if a in results:
                results[a] += 1

        return results
