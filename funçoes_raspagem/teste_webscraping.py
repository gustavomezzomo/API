from typing import List, Text
from bs4 import BeautifulSoup
import requests
from typing import Container
from cursos import *
from nomes import nome_equipes
import os

def raspar_2020_1():

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

    textfile = open("2020-1_file.txt", "w")
    for element in lista_grupo:
        textfile.write(element + "\n")
    textfile.close()

def raspar_2020_2():

    source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-2/turmas_2020-2.html').text

    soup = BeautifulSoup(source, 'lxml')

    text = [i for i in soup.find_all('td')]

    semestre_list = []
    for i in text [0:]:
        result = i.text.strip()
        semestre_list.append(result)

    textfile = open("2020-2_file.txt", "w")
    for element in semestre_list:
        textfile.write(element + "\n")
    textfile.close()

def raspar_2021_1():

    source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2021-1/turmas_2021-1.html').text

    soup = BeautifulSoup(source, 'lxml')

    text = [i for i in soup.find_all('td')]

    semestre_list = []
    for i in text [0:]:
        result = i.text.strip()
        semestre_list.append(result)

    textfile = open("2021-1_file.txt", "w")
    for element in semestre_list:
        textfile.write(element + "\n")
    textfile.close()
