from bs4 import BeautifulSoup
import csv
import requests

source=requests.get('http://www.hvg.hu/').text
soup=BeautifulSoup(source,'lxml')
csv_file=open('hvg_scrape.csv','w')
csv_writer=csv.writer(csv_file)

fg=soup.find_all('article')
for text in fg:
    text1=text.h1
    text2=text.a.text
    #text2=soup.get_text
    #print(text1)
    if text1==None:
        print("Something went wrong")
    else:
        csv_file.write(str(text2))
        print("File has been written")


csv_file.close()