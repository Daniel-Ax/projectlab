import csv
import logging
import pandas as pd
import numpy as np


news=[]
news_clean1=[]
with open('text', 'r', newline='',encoding='utf-8') as file:
    csv_f = csv.reader(file)
    for row in csv_f:
        print(row)
        news.append(row)



for i in news:
    print(i.strip())

# df = pd.DataFrame(data=news_clean1, dtype=np.int8)
# data = pd.read_csv("hvg_scrape.csv")