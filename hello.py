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

response = get_equipes().json()

# obj = json.loads(response)

pprint(response)
print response
