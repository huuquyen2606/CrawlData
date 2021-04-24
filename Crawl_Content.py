import pandas as pd
import requests
from bs4 import BeautifulSoup
import html2text
import csv
import collections

columns = collections.defaultdict(list)
with open('dataLink.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for index,row in enumerate(reader):
        for (k,v) in enumerate(row):
            if index != 0:
                columns[k].append(v)

dataContents = []

for index, link in enumerate(columns[1]):
    page = requests.get(link ,verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('div',class_='portlet-content')
    h = html2text.HTML2Text()
    h.ignore_links = True
    dataContents.append(h.handle(content[0].get_text()))
    print('Finished page '+ str(index))

linkTimeline ='https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs_delta=10&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs_cur='
for i in range(1,66):
    page = requests.get(linkTimeline + str(i) ,verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    for content in soup.find_all('div',class_='timeline'):
        h = html2text.HTML2Text()
        h.ignore_links = True
        dataContents.append(h.handle(content.get_text()))

df= pd.DataFrame({
                  'Content':dataContents
                })
df.transpose
df.to_csv(r'data.csv',index=False,header=True, encoding='utf-8')