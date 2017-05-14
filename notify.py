from selenium import webdriver
from pprint import pprint
from random import random
from datetime import datetime, timedelta
import time
from time import gmtime, strftime
import json
import requests
import urllib

HEADERS = {'token': 'hack2017-grupo3'}
URL_BASE = 'https://api.sde.globo.com/esportes/futebol/modalidades/futebol_de_campo/categorias/profissional'

def get_from_server(date,mandante,visitante):
    wd = webdriver.PhantomJS()
    url = "http://globoesporte.globo.com/rj/futebol/brasileirao-serie-a/jogo/{}/{}-{}/".format(date,mandante,visitante)
    wd.get(url = url)
    script = """
    function get(cls, x){ return $(x).find(cls).text(); }
    function get_img(x) {
      var $img = $(x).find(".thumb-midia-container > img");
      var src = $img.attr('src');
      var dataSrc = $img.data('src');
      return dataSrc || src;
    }
    function get_id(x) { return x.getAttribute("id"); }
    function get_data(x){
        return {
           id: get_id(x),
           time: get(".minuto-lance", x),
           period: get(".periodo-lance", x),
           title: get(".titulo-lance", x),
           img: get_img(x),
           desc: get(".descricao-lance", x)
        };
    }
    var data = $('.lance-a-lance-container .lance-normal[id]').map(function(i,x){ return get_data(x); } );
    return data;
    """
    return wd.execute_script(script)

fake = {}
fake['cache'] = None
fake['count'] = 0

def fake_get_from_server(date, mandante, visitante):
    if fake['cache'] == None:
        fake['cache'] = get_from_server(date, mandante, visitante)
        fake['cache'].reverse()

    step = round(random()*3)
    fake['count'] += step

    return fake['cache'][0:fake['count']]


mandante_arr = []
visitante_arr = []
date_arr = []
done_arr = []

seen = {}

def present(entry):
    desc = entry['desc'].strip()
    titulo = entry['title']
    timestr = entry['period']
    if entry['time'] != '':
        timestr = entry['time'] + ' ' + timestr

    msg = timestr + '\n' + titulo + '\n\n' + desc

    json = {
        'mandante': mandante,
        'visitante': visitante,
        'msg': msg}

    if entry['img']:
        json['img'] = entry['img']

    return json

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
def get_next_game(date_st, date_end):
	url = URL_BASE + '/campeonatos/campeonato-brasileiro/edicoes/campeonato-brasileiro-2017/jogos?data_hora_inicial=%s&data_hora_final=%s' % (date_st, date_end)
	resp = requests.get(url, headers=HEADERS).json()
	if ('jogos' in resp['resultados'].keys()):
		return resp['resultados']['jogos'][0],  resp['referencias']
	return "Não foram encontrado jogos futuros.", None

def update_minute():
    for i in range(len(date_arr)):
        if (done[i]):
            continue

        resp = fake_get_from_server(date_arr[i], mandante_arr[i], visitante_arr[i])
        for x in resp:
            if (x['id'] in seen):
                continue
            seen[x['id']] = True
            print("Sending msg id {}".format(x['id']))

            if (x['desc'] != '\n'):
                requests.post('http://a6824bbf.ngrok.io/sendRealTimeMessage/', json = {present(x)})


def notify_new_game(): 
    next_game, ref = get_next_game(strftime("%Y-%m-%dT%H:%M:%S", gmtime()), (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S"))
    pprint(next_game)
    # Notify torcedores e interessados.
    if ref is not None:
        date = next_game['data_realizacao']
        mandante = get_slug_by_equipe_id(next_game['equipe_mandante_id'])
        visitante = get_slug_by_equipe_id(next_game['equipe_visitante_id'])
        requests.post('http://a6824bbf.ngrok.io/notifyGame/', json = {'mandante': mandante, 'visitante': visitante})
        date_arr.append(date)
        mandante_arr.append(mandate)
        visitante_arr.append(visitante)
        done_arr.append(false)

while True:
    notify_new_game()

    for i in range(15):
        update_minute()
        time.sleep(60)
