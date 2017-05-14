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

def get_equipe_escudo_url_by_id(id):
	equipe = get_equipe_by_id(id)
	return equipe['escudos']['60x60']

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

def get_popular_name_by_slug(slug):
	equipes = query_equipes()['resultados']['equipes']
	for equipe in equipes:
		if (equipe['slug'] == slug):
			return equipe['nome_popular']
	return slug

def get_next_game_by_equipe_id_initial_date(equipe_id, initial_date = '2017-03-13'):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_inicial=%s' % (equipe_id, initial_date)
	response = requests.get(url, headers=HEADERS)
	return (response.json())['resultados']['jogos'][0]

def get_game_by_mandante_slug_visitante_slug_date(mandante_slug, date):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?equipe_id=%s&data_hora_inicial=%s&data_hora_final=%s' % (get_equipe_id_by_slug(mandante_slug), date, date)
	response = requests.get(url, headers=HEADERS)
	return response.json()

def get_nickname_from_slug(slug):
	# Upstream: http://nomeschiques.com/lista-de-25-apelidos-de-times-brasileiros-e-seus-rivais-humor/
	d = {
		'flamengo': 'Mengão',
		'vasco': 'Vascão',
		'botafogo': 'Fogão',
		'fluminense': 'Nense',
		'atlético-mg': 'Galo',
		'corinthians': 'Timão',
		'internacional': 'Inter',
	}
	return d.get(slug, slug)
