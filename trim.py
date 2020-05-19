import csv
import pandas as pd
import numpy as np
f=open('hvg_scrape.csv')
csv_f=csv.reader(f)
news=[]
news_clean1=[]
for row in csv_f:
    news.append(row)
f.close()

for i in news:
    if i or any(row) or any(field.strip('\t') for field in row):
        news_clean1.append(i)

df = pd.DataFrame(data=news_clean1, dtype=np.int8)
data = pd.read_csv("hvg_scrape.csv")