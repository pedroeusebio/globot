#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import requests
import urllib

# Docs:
#
# - esporte_slug = futebol
# - modalidade_slug = futebol_de_campo
# - categoria_slug = profissional
#                               /esportes/{esporte_slug}/modalidades/{modalidade_slug}/categorias/{categoria_slug}/campeonatos'

HEADERS = {'token': 'hack2017-grupo3'}
URL_BASE = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional'


def get_campeonatos():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/'
	return requests.get(url, headers=HEADERS)

def get_campeonato_brasileiro_2017():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos'
	return requests.get(url, headers=HEADERS)

def get_equipes():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/equipes'
	return requests.get(url, headers=HEADERS)

# -> List<String>
def get_equipes_popular_name_list():
	response = get_equipes().json()['resultados']['equipes']
	ret = []
	for t in response:
		ret.append(t['nome_popular'])
	return ret

# (266, '2017-05-01') -> dict
def get_next_game(team_id, date):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_inicial=%s' % (team_id, date)
	response = requests.get(url, headers=HEADERS)
	return (response.json())['resultados']['jogos'][0]

response = get_next_game(266, "2017-05-01")
pprint(response)

print get_equipes_popular_name_list()
