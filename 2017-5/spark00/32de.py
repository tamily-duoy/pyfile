#!python2
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

# urls = ["http://lishi.tianqi.com/guangzhou/201707.html",
#         "http://lishi.tianqi.com/guangzhou/201706.html",
#         "http://lishi.tianqi.com/guangzhou/201705.html"]


def req(year,month):
    urls=["http://lishi.tianqi.com/guangzhou/"+year+month+".html"]
    # return requests.get(url)

    for_return=[]
    # file = open('Guangzhou_weather.csv','w')
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
                    str += li.string.encode('utf-8')+ ','
                for_return.append(str)
                # if i!=0:
                #     file.write(str+'\n')

                # i+=1

    return for_return
    # file.close()

if __name__ == '__main__':
    result=[]
    # Y = ["2017","2015","2014","2013"]
    Y = ["2017"]
    # month = "7"





    result = []
    f = open('wunian_wea.txt', 'w+')
    for year in Y:
        # print(year)
        month = 1

        for x in range(month, 13):
            # print("============== %d 月 ==============" % x)
            month = str(x) if x > 9 else "0" + str(x)  # 小于10的月份要补0

            data = req(year, month)
            result.extend(data)
            time.sleep(1)

            # f = open("text12341.txt", 'w')
    for i in range(len(result)):
        f.write(str(result[i]))
        print(str(result[i]))