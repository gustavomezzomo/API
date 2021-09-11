from os import replace
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

source = requests.get('https://fatecsjc-prd.azurewebsites.net/api/2020-2/turmas_2020-2.html').text

soup = BeautifulSoup(source, 'lxml')

links = [i['href'] for i in soup.find_all('a', href=True)]

links_list = []
for i in links [0:]:
    result = i
    links_list.append(result)

print (links_list)

c = 0

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

link_list = []

while c < len(links_list):
    url = links_list[c]
    c = c+1
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.get(url)

    link = [i['href'] for i in soup.select('div#meta div#description [href]')]
    link_list.append(link)
driver.quit()

print (link_list)