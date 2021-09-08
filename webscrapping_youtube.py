from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.youtube.com/watch?v=gqUqGaXipe8').text

soup = BeautifulSoup(source, 'lxml')

link = [i['href'] for i in soup.findAll('a', class_='yt-simple-endpoint style-scope yt-formatted-string', href=True)]

print(link)
