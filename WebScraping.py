from bs4 import BeautifulSoup
import requests

source=requests.get('http://hvg.hu/').text
soup= BeautifulSoup(source,'lxml')
print(soup.prettify())

