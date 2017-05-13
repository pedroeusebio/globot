#!/usr/bin/env python

import requests

url = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional/campeonatos/campeonato-brasileiro/edicoes/'

# url = 'https://api.sde.globo.com/esportes'
headers = {'token': ''}

response = requests.get(url, headers=headers).json()
print response['resultados']
