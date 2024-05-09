# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:45:21 2024

@author: h6173
"""
import requests
from bs4 import BeautifulSoup
#地震資訊爬蟲
#取得中央氣象局會員API授權碼:CWA-EC693080-AFF8-4B5C-94F5-44DE876C0F80
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWA-EC693080-AFF8-4B5C-94F5-44DE876C0F80'  #地震資訊JSON網址

#發送GET請求
response = requests.get(url)
#獲取JSON數據
data_json = response.json()
earthquake = data_json['records']['Earthquake']  #轉換成json格式

for i in earthquake:
    loc = i['EarthquakeInfo']['Epicenter']['Location']
    val = i['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue']
    dep = i['EarthquakeInfo']['FocalDepth']#['value']
    eq_time = i['EarthquakeInfo']['OriginTime']
    img = i['ReportImageURI']
    msg = f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}'
    print(msg)
    
    token = 'LINE Notify 權杖'
    headers = {
        'Authorization' : 'Bearer ' + 'KZMTn522OdIPROZ9iDcGGg2DJkf9RPjRtOh68cTCr2L'
    }
    data = {
        'message':msg, 
        'imageThumbnail':img,
        'imageFullsize':img
        #'message':'測試一下！'     # 設定要發送的訊息

    }
    data = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
    break
