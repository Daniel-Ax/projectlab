from bs4 import BeautifulSoup
import csv
import requests

source=requests.get('http://www.hvg.hu/').text
soup=BeautifulSoup(source,'lxml')
csv_file=open('hvg_scrape.csv','w')
csv_writer=csv.writer(csv_file)

fg=soup.find_all('div')
for text in fg:
    text1=text.h1
    print(text1)
    if text1==None:
        csv_file.write("Empty text")
    else:
        csv_file.write(str(text1))


