# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/9/17'

import json
import urllib2

from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0"
}

request = urllib2.Request(url, headers=headers)
html = urllib2.urlopen(request).read()

#解析为HTML DOM模式
text = etree.HTML(html)

#泛会所有段子的节点位置
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')
items = {}
for node in node_list:
    username = node.xpath('.//div//h2')[0].text
    image = node.xpath('.//img//@src')[0]
    content = node.xpath('.//div[@class="content"]/span')[0].text
    zan = node.xpath('.//i')[0].text
    comments = node.xpath('.//i')[1].text

    items = {
        "username" : username,
        "image" : image,
        "content": content,
        "zan": zan,
        "comments":comments
    }

    with open("qiushi.json","a") as f:
        f.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")

