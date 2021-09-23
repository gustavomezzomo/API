from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests

source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-1/turmas_2020-1.php').text

soup = BeautifulSoup(source, 'lxml')

#busca no link de source onde existe o href dentro de uma tag de link 'a' e gera uma lista com todos que encontrar
link_turmas = [i['href'] for i in soup.find_all('a', href=True)]



#variável utilizada somente para mudar o índice
var2 = 0

#lista vazia para acumular o index alterado fora do loop
l = []
while var2 <= 9:
  
    var = 'https://fatecsjc-prd.azurewebsites.net/api/2020-1/' +link_turmas[var2]
    var2 = var2 + 1
    l.append(var)