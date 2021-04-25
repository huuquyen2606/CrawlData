import pandas as pd
import requests
from bs4 import BeautifulSoup
import html2text
import csv
import collections
from csv import DictWriter
import time

def addRow (fileName, newrow):
    fields=['Content']
    with open(fileName, 'a',encoding="utf8") as file:
        content = DictWriter(file, fields)
        content.writerow({'Content':newrow})
        file.close()

# Crawl VnExpress content
numPagesNull = 0 
columns = collections.defaultdict(list)
with open('dataVnExpressLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for index,row in enumerate(reader):
        for (k,v) in enumerate(row):
            if index != 0:
                columns[k].append(v)
    file.close()
for index, link in enumerate(columns[1]):
    page = requests.get(link ,verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('article',class_='fck_detail')
    description = soup.find_all('p',class_='description')
    title = soup.find_all('h1', class_='title-detail')
    if (len(content)==0 or len(description)==0 or len(title)==0):
        numPagesNull+=1
    else:
        h = html2text.HTML2Text()
        h.ignore_links = True
        addRow('test.csv',h.handle(title[0].get_text()+'. '+description[0].get_text()+content[0].get_text()))
        print('Finished page '+ str(index))
print('Total page null:', numPagesNull)