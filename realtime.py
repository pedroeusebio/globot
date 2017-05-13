from selenium import webdriver
from pprint import pprint
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
pprint(wd.execute_script(script))
