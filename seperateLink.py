import pandas as pd
import requests
from bs4 import BeautifulSoup
import html2text
import csv
import collections
from csv import DictWriter
import time

# Crawl VnExpress content
columns = collections.defaultdict(list)
links = []
total = 1
with open('dataVnExpressLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for index,row in enumerate(reader):
        for (k,v) in enumerate(row):
            if index != 0:
                columns[k].append(v)
        if (index % 400 ==0 or index ==31141) and index != 0:
            links = columns[1][index-400:index-1]
            if index ==31141:
                links = columns[1][30800:31141]
            df= pd.DataFrame({
                        'Content':links
                        })
            df.transpose
            df.to_csv(r'LinkVnEx/data'+str(total)+'.csv',index=False,header=True, encoding='utf-8')
            total+=1
