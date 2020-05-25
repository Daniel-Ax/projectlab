from bs4 import BeautifulSoup
import csv
import requests
import re
import pandas as pd

source=requests.get('http://www.hvg.hu/').text
soup=BeautifulSoup(source,'lxml')
csv_file=open('hvg_scrape.csv','w')
csv_writer=csv.writer(csv_file)
fg=soup.find_all('article')


for text in fg:
    text1=text.h1
    text2=text.a
    text_final=soup.get_text()
    #text2=soup.get_text
    #print(text1)
    if text1==None:
        print("Something went wrong")
    else:
        with open('hvg_scrape.csv', 'w', newline='',encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(text_final)
            print("File has been written")



csv_file.close()