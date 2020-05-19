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
        print(text_final)
        #csv_file.write(str(text_final))
        print("File has been written")


csv_file.close()

# csv_final=open('pretty.csv','w')
# df = pd.read_csv('hvg_scrape.csv')
# pretty=df.to_csv('pretty.csv', index=False)
# writer=csv.writer(pretty)
#
# for i in len(pretty):
#     csv_final.write(str(pretty))
#
# csv_final.close()