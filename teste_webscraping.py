from bs4 import BeautifulSoup

import requests

html = requests.get("https://github.com/gustavomezzomo/livro-receitas").content

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('SSH'))