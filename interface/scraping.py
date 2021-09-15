from PySimpleGUI import PySimpleGUI as sg
from typing import List, Text
from bs4 import BeautifulSoup
import requests

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('bem vindo ao nosso executável de raspagem!!')],
    [sg.Button('raspar')],
]

#janela
janela = sg.Window('Tela de raspagem', layout)

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