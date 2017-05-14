# -*- coding: utf-8 -*-

Conversations = {}
Users = {}

def find_all_users_by_team(team_id):
	ret = []

	for recipient_id, user in Users:
		if user.team_id == team_id:
			ret.append(recipient_id)

	return ret