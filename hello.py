#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: noet

from pprint import pprint
import json
import requests
import urllib

HEADERS = {'token': 'hack2017-grupo3'}
URL_BASE = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional'


def query_campeonatos():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/'
	return requests.get(url, headers=HEADERS).json()

def query_campeonato_brasileiro_2017():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos'
	return requests.get(url, headers=HEADERS).json()

def query_equipes():
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/equipes'
	return requests.get(url, headers=HEADERS).json()

def get_equipe_by_id(id):
	equipes = query_equipes()['resultados']['equipes']
	for equipe in equipes:
		if int(equipe['equipe_id']) == id:
			return equipe
	return None

def get_equipe_by_slug(slug):
	equipes = query_equipes()['resultados']['equipes']
	for equipe in equipes:
		if equipe['slug'] == slug:
			return equipe
	return None

def get_slug_by_equipe_id(id):
	equipes = query_equipes()['resultados']['equipes']
	for equipe in equipes:
		if equipe['equipe_id'] == id:
			return equipe['slug']
	return None

def get_equipe_id_by_slug(slug):
	equipes = query_equipes()['resultados']['equipes']
	for equipe in equipes:
		if equipe['slug'] == slug:
			return equipe['equipe_id']
	return None

def get_list_of_equipes_popular_names():
	equipes = query_equipes()['resultados']['equipes']
	ret = []
	for equipe in equipes:
		ret.append(equipe['nome_popular'])
	return ret

def get_next_game_by_equipe_id(equipe_id, initial_date):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_inicial=%s' % (equipe_id, initial_date)
	response = requests.get(url, headers=HEADERS)
	return (response.json())['resultados']['jogos'][0]

pprint(get_list_of_equipes_popular_names())
