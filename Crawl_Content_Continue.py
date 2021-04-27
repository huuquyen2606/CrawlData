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
with open('dataDantriLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for index,row in enumerate(reader):
        for (k,v) in enumerate(row):
            if index != 0:
                columns[k].append(v)
    file.close()
headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        # "Accept-Encoding": "*",
        # "Connection": "keep-alive"
    }
for index, link in enumerate(columns[1]):
    link = 'https://dantri.com.vn/'+link
    checkError = False
    try:
        page = requests.get(link ,headers=headers)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        # raise SystemExit(e)
        print(e)
        # checkError =True
        time.sleep(180)
    print(page.status_code)
    # or checkError
    if int(page.status_code)!=200 :
        time.sleep(180)
        numPagesNull+=1
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find_all('div',class_='dt-news__body')
        
        if len(content)==0:
            numPagesNull+=1
        else:
            title = soup.find_all('h1',class_='dt-news__title')
            description = content[0].find_all('div', class_='dt-news__sapo')
            content_inside = content[0].find_all('div', class_='dt-news__content')
            h = html2text.HTML2Text()
            h.ignore_links = True
            addRow('DantriData.csv',h.handle(title[0].get_text()+'. '+description[0].get_text()+content_inside[0].get_text()))
            print('Finished page '+ str(index))
    break
print('Total page null:', numPagesNull)