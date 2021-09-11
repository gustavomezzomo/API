from typing import List, Text
from bs4 import BeautifulSoup
import requests

source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-2/turmas_2020-2.html').text

soup = BeautifulSoup(source, 'lxml')

text = [i for i in soup.find_all('td')]

semestre_list = []
for i in text [0:]:
    result = i.text.strip()
    semestre_list.append(result)

print(semestre_list)

textfile = open("semestre_file.txt", "w")
for element in semestre_list:
    textfile.write(element + "\n")
textfile.close()