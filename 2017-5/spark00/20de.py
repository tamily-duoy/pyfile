# encoding=utf-8
import requests
import json
import pymongo
import time
import os

def request(year, month):
    # url = "http://d1.weather.com.cn/calendar_new/" + year + "/101280701_" + year + month + ".html?_=1495685758174"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    #     "Referer": "http://www.weather.com.cn/weather40d/101280701.shtml",
    # }
    # http: // www.weather.com.cn / weather40d / 101280101.shtml
    #http://d1.weather.com.cn/calendar_new/2017/101280101_201711.html?_=1512372790036
    #"User-Agent":Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
    #http://www.weather.com.cn/weather40d/101280101.shtml
    url = "http://d1.weather.com.cn/calendar_new/" + year + "/101280101_" + year + month + ".html?_=1512372790036"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Referer": "http://www.weather.com.cn/weather40d/101280101.shtml",
    }

    return requests.get(url, headers=headers)

def parse(res):
    json_str = res.content.decode(encoding='utf-8')[11:]
    return json.loads(json_str)

def save(list):
    subkey = {'date': '日期', 'hmax': '最高温度', 'hmin': '最低温度', 'hgl': '湿度', 'fe': '节日', 'wk': '星期', 'time': '发布时间'}
    for_return = []
    for dict in list:
        subdict = {value: dict[key] for key, value in subkey.items()}   #提取原字典中部分键值对，并替换key为中文
        # print(subdict)
        for_return.append(subdict)
        forecast.insert_one(subdict)                                    #插入mongodb数据库
    return for_return








if __name__ == '__main__':
    # year = "2017"
    # month = 12

    Y=["2017"]
    # Y = ["2017"]

    client = pymongo.MongoClient('localhost', 27017)  # 连接mongodb,端口27017
    test = client['test']  # 创建数据库文件test
    forecast = test['forecast']


    result=[]
    f = open("test00.txt", 'w+')
    for year in Y:
        print(year)
        month=1

        for x in range(month, 13):

            # print("============== %d 月 ==============" % x)
            month = str(x) if x > 9 else "0" + str(x)  # 小于10的月份要补0

            data=save(parse(request(year, month)))
            result.extend(data)
            time.sleep(1)

            # f = open("text12341.txt", 'w')
    for i in range(len(result)):
        f.write(str(result[i]))


    # f.write(result)





