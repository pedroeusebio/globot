#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import requests
import urllib

HEADERS = {'token': 'hack2017-grupo3'}
URL_BASE = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional'


def get_stadium_name(ref, stadium_id):
	return ref['sedes'][str(stadium_id)]['nome_popular']

def get_team_name(ref, team_id):
	return ref['equipes'][str(team_id)]['nome_popular']

#   Game Raw Data Example
# 	{u'cancelado': False,
#	 u'data_realizacao': u'2017-05-14',
#	 u'decisivo': False,
#	 u'equipe_mandante_id': 266,
#	 u'equipe_visitante_id': 277,
#	 u'escalacao_mandante_id': 451761,
#	 u'escalacao_visitante_id': 451758,
#	 u'fase_id': 5196,
#	 u'hora_realizacao': u'11:00:00',
#	 u'jogo_id': 211239,
#	 u'placar_oficial_mandante': None,
#	 u'placar_oficial_visitante': None,
#	 u'placar_penaltis_mandante': None,
#	 u'placar_penaltis_visitante': None,
#	 u'rodada': 1,
#	 u'sede_id': 277,
#	 u'suspenso': False,
#	 u'vencedor_jogo': None,
#	 u'wo': False}
def get_next_game(team_id, date):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_inicial=%s' % (team_id, date)
	resp = requests.get(url, headers=HEADERS).json()
	if ('jogos' in resp['resultados'].keys()):
		return resp['resultados']['jogos'][0],  resp['referencias']
	return "Nao foram encontrado jogos futuros.", None

# Formato da resposta:
#  Campeonato Brasileiro 2017
#  Dia, Horario
#  Estadio
#  (logo) meu_time x time_adversario (logo)
#
def get_next_game_formatted(team_id, date):
	game_info, ref = get_next_game(team_id, date)
	if (ref is None):
		return game_info
	dia = game_info['data_realizacao']
	horario = game_info['hora_realizacao']
	estadio = get_stadium_name(ref, game_info['sede_id'])
	timeA = get_team_name(ref, game_info['equipe_visitante_id'])
	timeB = get_team_name(ref, game_info['equipe_mandante_id'])
	#TODO: add logo for teams
	return '''Campeonato Brasileiro 2017\n%s, %s\n%s\n%s x %s\n''' % (dia, horario, estadio, timeA, timeB)

def get_last_game(team_id, date):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_final=%s&ord=desc' % (team_id, date)
	resp = requests.get(url, headers=HEADERS).json()
	#pprint(resp)
	if ('jogos' in resp['resultados'].keys()):
		return resp['resultados']['jogos'][0],  resp['referencias']
	return "Nao foram encontrado jogos anteriores.", None

def get_last_game_formatted(team_id, date):
	game_info, ref = get_last_game(team_id, date)
	if (ref is None):
		return game_info
	dia = game_info['data_realizacao']
	horario = game_info['hora_realizacao']
	estadio = get_stadium_name(ref, game_info['sede_id'])
	timeA = get_team_name(ref, game_info['equipe_visitante_id'])
	timeB = get_team_name(ref, game_info['equipe_mandante_id'])
	scoreA = game_info['placar_oficial_visitante']
	scoreB = game_info['placar_oficial_mandante']
	#TODO: add logo for teams
	return '''Campeonato Brasileiro 2017\n%s, %s\n%s\n%s %s - %s %s\n''' % (dia, horario, estadio, timeA, scoreA, scoreB, timeB)

#url = 'https://api.sde.globo.com/jogos/211240/scouts'

#response = get_next_game_formatted(266, "2017-05-01")
#print(response)

# print get_equipes_popular_name_list()
