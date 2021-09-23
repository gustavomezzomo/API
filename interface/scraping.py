from PySimpleGUI import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
from tkinter import *
from semestre import Semestres

#layout
sg.theme('BlueMono')
layout = [
    [sg.Text('bem vindo a nossa interface de raspagem!!')],
    [sg.Text('essa interface tem por objetivo fazer a raspagem de dados dos grupos de API dos semestres já finalizados,')],
    [sg.Text('salvando os mesmos em um banco de dados e disponibilizando-os para consulta enquanto mantém os dados salvos!')],
    [sg.Button('raspar')],
]

#janela
janela = sg.Window('Nossa interface de raspagem', layout, element_justification='c')

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'raspar':
        source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-2/turmas_2020-2.html').text

        soup = BeautifulSoup(source, 'lxml')

        text = [i for i in soup.find_all('td')]

        semestre_list = []
        for i in text [0:]:
            result = i.text.strip()
            semestre_list.append(result)

        textfile = open("raspagem.txt", "w")
        for element in semestre_list:
            textfile.write(element + "\n")
        textfile.close()