import pandas as pd
import requests
from bs4 import BeautifulSoup

dataTitles = []
dataDates = []
dataLinks = []
#842 tin tuc
#22 dieu can biet
#36 khuyen cao
#66 timeline
linkGov = [
  ['https://ncov.moh.gov.vn/vi/web/guest/tin-tuc?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_uNo2VNPYc2UM&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_uNo2VNPYc2UM_delta=5&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_uNo2VNPYc2UM_cur=',843],
  ['https://ncov.moh.gov.vn/vi/web/guest/-ieu-can-biet?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_f0F16up2JteV&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_f0F16up2JteV_delta=5&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_f0F16up2JteV_cur=',23],
  ['https://ncov.moh.gov.vn/vi/web/guest/khuyen-cao?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_0XHNjAbqHvlQ&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_0XHNjAbqHvlQ_delta=5&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_0XHNjAbqHvlQ_cur=',37]
]
linkVnEx = ['https://vnexpress.net/suc-khoe-p',1039]
linkVietNamNet = ['https://vietnamnet.vn/vn/suc-khoe/trang',540]
# #Crawl from Goverment
# for pageRange in range(3):
#   for i in range(1,int(linkGov[pageRange][1])):
#     link = str(linkGov[pageRange][0]) + str(i)
#     page = requests.get(link,verify=False)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     for element in soup.find_all('div', class_='row mb-1'):
#       titles = element.find_all('a',class_='text-tletin')
#       # dates = element.find_all('small',class_='text-muted')
#       hrefs = element.find_all('a', class_='text-tletin')
#       dataTitles.append(titles[0].get_text())
#       # dataDates.append(dates[0].get_text())
#       dataLinks.append(hrefs[0]['href'])
#     print('Finished page '+ str(i))

#Crawl from vnexpress
# for i in range(1,int(linkVnEx[1])):
#   link = str(linkVnEx[0]) + str(i)
#   page = requests.get(link,verify=False)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   for element in soup.find_all('h3',class_='title-news'):
#     titles = element.find_all('a')
#     dataTitles.append(titles[0].get_text())
#     dataLinks.append(titles[0]['href'])
#   for element in soup.find_all('h2',class_='title-news'):
#     titles = element.find_all('a')
#     dataTitles.append(titles[0].get_text())
#     dataLinks.append(titles[0]['href'])
#   print('Finished page '+ str(i))

#Crawl from vietnamnet
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
for i in range(1,int(linkVietNamNet[1])):
  link = str(linkVietNamNet[0]) + str(i) +'/'
  page = requests.get(link,headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  for element in soup.find_all('div',class_='clearfix item'):
    titles = element.find_all('a',class_='f-18 title')
    dataTitles.append(titles[0].get_text())
    dataLinks.append(titles[0]['href'])
  print('Finished page '+ str(i))
df= pd.DataFrame({
                'titles':dataTitles,
              #   'dates':dataDates,
                'links':dataLinks
              })
df.transpose
df.to_csv(r'dataVNNet.csv',index=False,header=True, encoding='utf-8')