from bs4 import BeautifulSoup
import csv
import requests

source=requests.get('http://www.hvg.hu/').text
soup=BeautifulSoup(source,'lxml')
csv_file=open('hvg_scrape.csv','w')
csv_writer=csv.writer(csv_file)