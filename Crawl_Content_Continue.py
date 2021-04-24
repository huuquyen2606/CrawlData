import pandas as pd
import requests
from bs4 import BeautifulSoup
import html2text
import csv
import collections
from csv import DictWriter



# Crawl VnExpress content
columns = collections.defaultdict(list)
links = []
with open('dataVnExpressLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for index,row in enumerate(reader):
        for (k,v) in enumerate(row):
            if index != 0:
                columns[k].append(v)

def addRow (fileName, newrow):
    fields=['Content']
    with open(fileName, 'a',encoding="utf8") as file:
        content = DictWriter(file, fields)
        content.writerow({'Content':newrow})
        file.close()
#Add more row 
dataContents= []
for index, link in enumerate(columns[1]):
    page = requests.get(link ,verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('article',class_='fck_detail')
    description = soup.find_all('p',class_='description')
    title = soup.find_all('h1', class_='title-detail')
    h = html2text.HTML2Text()
    h.ignore_links = True
    dataContents.append(h.handle(title[0].get_text()+'. '+description[0].get_text()+content[0].get_text()))
    print('Finished page '+ str(index))

df= pd.DataFrame({
                  'Content':dataContents
                })
df.transpose
df.to_csv(r'data1.csv',index=False,header=True, encoding='utf-8')