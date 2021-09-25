from typing import List, Text
from bs4 import BeautifulSoup
import requests

source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-1/turmas_2020-1.php').text

soup = BeautifulSoup(source, 'lxml')

link = [i['href'] for i in soup.find_all('a', href=True)]

var2 = 0
lista_link = []
lista_grupo = []
var3 = 0

while var2 <= 10:

    var = 'https://fatecsjc-prd.azurewebsites.net/api/2020-1/' +link[var2]
    lista_link.append(var)
    var2 = var2 + 1

while var3 <=10:
    source = requests.get(lista_link[var3]).text
    soup = BeautifulSoup(source, 'lxml')
    text = [i for i in soup.find_all('a', text=True)]
    link = [i['href'] for i in soup.find_all('a', href=True)]
    lista_grupo.append(text)
    lista_grupo.append(link)
    var3 = var3 + 1

print(lista_grupo)