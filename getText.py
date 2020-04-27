from bs4 import BeautifulSoup
import requests

source=requests.get('http://www.hvg.hu/')
soup = BeautifulSoup(source)
text = soup.get_text()
print(text)