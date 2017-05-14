import facebook
import secrets

VERSION = '/v2.9/'

graph = facebook.GraphAPI(secrets.ACCESS_TOKEN)

class TeamSlugFilter():
    def __init__(self, slug):
        self.slug = slug

    def test(self, user):
        return user.team_slug == self.slug

class User:
    def __init__(self, recipient_id):
        self.recipient_id = recipient_id
        self.team_slug = None
        self.team_id = None
        self.name = self.get_name(recipient_id)

    def get_name(self, recipient_id):
        query = VERSION + str(recipient_id)
        data = graph.request(query)
        for key in ['first_name', 'name', 'last_name']:
            if key in data:
                return data[key]
        return "colega"
