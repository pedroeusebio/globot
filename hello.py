#!/usr/bin/env python

import json
import requests

# Docs:
#
# - esporte_slug = futebol
# - modalidade_slug = futebol_de_campo
# - categoria_slug = profissional
#                               /esportes/{esporte_slug}/modalidades/{modalidade_slug}/categorias/{categoria_slug}/campeonatos'

URL_BASE = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional'
HEADERS = {'token': 'hack2017-grupo3'}

# url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/'
url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos'

response = requests.get(url, headers=HEADERS).json()

print response['resultados']
