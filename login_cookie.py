# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/8/17'

import urllib2

url = "http://www.lagou.com/resume/myresume.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Cookie":"***",
    "Host":"www.lagou.com",
    "Connection":"keep-alive",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh,en-US;q=0.8,en;q=0.6,zh-CN;q=0.4",

}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print response.read()
