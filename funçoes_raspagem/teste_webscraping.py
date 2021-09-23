from typing import List, Text
from bs4 import BeautifulSoup
import requests
from typing import Container
from cursos import *
from nomes import nome_equipes
import os

def raspar_2020_1():

    contador = 0

    ads12020 = [todos[0]]
    y = []

    while contador <= len(ads12020[0]) - 1:
        x = f'{nome_equipes[contador]} {ads12020[0][contador]}'
        y.append(x)
        contador = contador + 1
    with open('1ºADS-Turma A', 'w', newline='') as file:
        for line in y:
            file.write(line + os.linesep)

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
