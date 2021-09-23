from typing import List, Text
from bs4 import BeautifulSoup
import requests
from Turmas1sem import l

contador = 0
nome_equipes = []

l_l = len(l)

while contador <= l_l - 1:
    source = requests.get(l[contador]).text

    soup = BeautifulSoup(source, 'lxml')

    text = [i for i in soup.find_all('a')]
    
    contador = contador + 1
    for i in text [0:]:
        result = i.text.strip()
        
        nome_equipes.append(result)