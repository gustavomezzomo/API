from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)
url = 'https://www.youtube.com/watch?v=gqUqGaXipe8'
driver.get(url)
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


link = [i['href'] for i in soup.select('div#meta div#description [href]')]
print(link)