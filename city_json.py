# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/9/17'

import urllib2
import json
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0"
}

request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)

html = response.read()

unicodestr = json.loads(html)

#python形势列表
city_list = jsonpath.jsonpath(unicodestr, "$..name")

for item in city_list:
    print item

array = json.dumps(city_list, ensure_ascii=False)
with open("lagoucity.json","w") as f:
    f.write(array.encode("utf-8"))

