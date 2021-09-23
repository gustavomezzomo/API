from bs4 import BeautifulSoup
from bs4.builder import HTMLTreeBuilder
from bs4.element import ResultSet
import requests
from Turmas1sem import l
from nomes import nome_equipes



n_e = len(l)
link_youtube = []
contador = 0
todos = []

while contador <= n_e - 1:
    fonte = requests.get(l[contador]).text
    sopa = BeautifulSoup(fonte, 'lxml')

    links_equipes = [link['href'] for link in sopa.findAll('a', href=True)]
    todos.append(links_equipes)
    contador = contador + 1