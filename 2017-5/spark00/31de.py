#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

urls = ["http://lishi.tianqi.com/wuhan/201707.html",
        "http://lishi.tianqi.com/wuhan/201706.html",
        "http://lishi.tianqi.com/wuhan/201705.html"]



file = open('wuhan_weather.csv','w')
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_list = soup.select('div[class="tqtongji2"]')

    for weather in weather_list:
        weather_date = weather.select('a')[0].string.encode('utf-8')
        ul_list = weather.select('ul')
        i=0
        for ul in ul_list:
            li_list= ul.select('li')
            str=""
            for li in li_list:
                str += li.string.encode('utf-8')+','
            print(str)
            if i!=0:
                file.write(str+'\n')
            i+=1
file.close()