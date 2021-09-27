from typing import List, Text
from bs4 import BeautifulSoup
import requests
from functools import *

source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-1/turmas_2020-1.php').text

soup = BeautifulSoup(source, 'lxml')

link = [i['href'] for i in soup.find_all('a', href=True)]

var2 = 0
lista_link = []
lista_nomes = []
lista_turma = []
var3 = 0

while var2 <= 10:

    var = 'https://fatecsjc-prd.azurewebsites.net/api/2020-1/' +link[var2]
    lista_link.append(var)
    var2 = var2 + 1
    
while var3 <=10:
    source = requests.get(lista_link[var3]).text
    soup = BeautifulSoup(source, 'lxml')
    turma = [i for i in soup.find_all('h3')]
    for i in turma [0:]:
        nome = i.text.strip()
    lista_turma.append(nome)
    text = [i for i in soup.find_all('a', href=True)]
    for x in text [0:]:
        lista_nomes.append(x.text.strip())
    link = [i['href'] for i in soup.find_all('a', href=True)]
    while True:
        try:
            lista_turma.append(lista_nomes.pop(0))
            lista_turma.append(link.pop(0))
        except IndexError:
            break
    var3 = var3 + 1



textfile = open("2020-1_file.txt", "w")
for element in lista_turma:
        textfile.write(element + "\n")
textfile.close()