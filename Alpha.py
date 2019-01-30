# coding=UTF-8
from bs4 import BeautifulSoup
import time
import os
import requests
import warnings
import threading
import pandas as pd
warnings.filterwarnings('ignore')
T1 = time.time()
df = pd.DataFrame()

# 以下為標題抓取

def title() :
    Page = 1
    with open('Sanlih.txt',"w",encoding='utf-8') as files:
        while True :
            Page+=1
            try:
                src1 = 'https://www.setn.com/ViewAll.aspx?p='+str(Page)
                print("正在處理第"+str(Page)+"頁：")
                response = requests.get(src1)
                html = BeautifulSoup(response.text)
                NewsList = html.find('div', class_='row NewsList')
                if NewsList == "":
                    break
                print(NewsList)
                column = NewsList.find_all('div', class_='col-sm-12')
                for vital in column:
                    title = vital.find('h3', class_='view-li-title')
                    times = vital.find('time', style='color: #a2a2a2;')
                    category = vital.find('div', class_='newslabel-tab')
                    url2 = vital.find('h3', class_='view-li-title')
                    urls = url2.find('a')['href']
                    splits =urls.split('/')
                    # print(splits)
                    if splits[1]  == 'e':
                        urls = "https://www.setn.com/" + splits[2]
                    elif splits[1].startswith('News'):
                        urls = "https://www.setn.com" + urls
                    else:
                        continue

                    # print(title(a)[href])
                    # print('發佈時間：',times.text)
                    # print('分類：',category.text)
                    # print('標題：',title.text)
                    # print('網址：',urls)
                    # print(times.text.split(" ")[0])
            except:
                break
            files.write(urls)
            if Page == 2 :
                break

t = threading.Thread(target=title)
t.start()
t.join()
T2 = time.time()
print("標題抓取總共花了"+str(T2-T1)+"秒")

# 以下為內文抓取

# z=0
# with open("Text.txt","w",encoding="utf-8") as file:
#     while True:
#         try:
#             z+=1
#             src2 = 'https://www.setn.com/ViewAll.aspx?p='+str(z)
#             print("正在處理第"+str(z)+"頁：")
#             response = requests.get(src2)
#             html = BeautifulSoup(response.text)
#             NewsList = html.find('div', class_='row NewsList')
#             column = NewsList.find_all('div', class_='col-sm-12')
#             for vital in column:
#                 url2 = vital.find('h3', class_='view-li-title')
#                 urls = url2.find('a')['href']
#                 splits =urls.split('/')
#                 # print(splits)
#                 if splits[1]  == 'e':
#                     urls = "https://www.setn.com" + urls
#                 elif splits[1].startswith('News'):
#                     urls = "https://www.setn.com/e" + urls
#                 else :
#                     continue
#                 src3 = urls
#                 response2 = requests.get(src3)
#                 html2 = BeautifulSoup(response2.text)
#                 content2 = html2.find('div', class_='Content2')
#                 Keyword = html2.find('div',class_='keyword')
#                 print(content2.text)
#                 print(Keyword.text)
#                 keyword_list = []
#                 for keyword2 in Keyword.text:
#                     keyword_list.append(keyword2.text)
#                 print("This is : "+keyword_list)
#         except:
#             continue
# T3 = time.time()
# print("內文抓取總共花了"+str(T3-T2)+"秒")



