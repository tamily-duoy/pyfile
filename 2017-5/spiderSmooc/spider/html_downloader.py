#coding:utf-8
"""爬虫的核心内容1：下载器"""
# import cookielib
import urllib
# import urllib2
from urllib.parse import urlparse
from urllib.request import urlopen
class Html_Downloader(object):
    '''
    这个类主要是下载html使用的是urllib2模块
    '''
    def download(self, url):
        if url is None:
            return None
        # request = urllib2.Request(url)
        request = urllib.Request(url)   #创建request对象
        #下面的两个header是为了模拟手机浏览器，
        # 因为慕课网app可以不用注册就可以访问视频，
        # 所以把咱们的程序模拟成手机浏览器，就可以直接下载了
        request.add_header('user-agent',            #添加http的header
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
        request.add_header('host','www.imooc.com')
        # response= urllib2.urlopen(request)
        response = urllib.urlopen(request)   #发送请求获取结果
        if response.getcode()!=200:
            return None
        return response.read()