from selenium import webdriver
from pprint import pprint
from random import random
import requests
import time

url = 'http://globoesporte.globo.com/rj/futebol/brasileirao-serie-a/jogo/13-05-2017/flamengo-atletico-mg/'

wd = webdriver.PhantomJS()
wd.get(url = url)
script = """
function get_time(x){ return $(x).find(".tempo-lance").text(); }
function get_desc(x){ return $(x).find(".descricao-lance").text(); }
function get_id(x) { return x.getAttribute("id"); }
function get_data(x){
    return {
       id: get_id(x),
       time: get_time(x),
       desc: get_desc(x)
    };
}
var data = $('.lance-a-lance-container .lance-normal[id]').map(function(i,x){ return get_data(x); } );
return data;
"""

def get_from_server():
	return wd.execute_script(script)

fake = {}
fake['cache'] = None
fake['count'] = 0

def fake_get_from_server():
	if fake['cache'] == None:
		fake['cache'] = get_from_server()
		fake['cache'].reverse()

	step = round(random()*3)
	fake['count'] += step

	return fake['cache'][0:fake['count']]


mandante = "flamengo"
visitante = "atletico-mg"

seen = {}

def present(entry):
	return entry['desc']

while True:
	arr = []
	resp = fake_get_from_server()
	for x in resp:
		if (x['id'] in seen):
			continue
		seen[x['id']] = True
		print("Sending msg id {}".format(x['id']))

		if (x['desc'] != '\n'):
			requests.post('http://a6824bbf.ngrok.io/sendRealTimeMessage/', json = {'mandante': mandante, 'visitante': visitante, 'msg': present(x)})
			
		
	time.sleep(5)