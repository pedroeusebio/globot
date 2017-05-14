from selenium import webdriver
from pprint import pprint
from random import random
import requests
import time


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


mandante = "flamengo"
visitante = "atletico-mg"
date = "13-05-2017"

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

while True:
    arr = []
    resp = fake_get_from_server(date, mandante, visitante)
    for x in resp:
        if (x['id'] in seen):
            continue
        seen[x['id']] = True
        print("Sending msg id {}".format(x['id']))

        if (x['desc'] != '\n'):
            requests.post('http://a6824bbf.ngrok.io/sendRealTimeMessage/', json = present(x))

    time.sleep(5)
