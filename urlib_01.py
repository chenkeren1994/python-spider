# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/8/17'

import urllib2
import urllib
import random


#爬取百度贴吧


def loadPage(url,filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url : 需要爬去的url地址
        filename:处理的文件名
    :return:
    """
    print "【正在下载】"+ filename

    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }



    request = urllib2.Request(url, headers = headers)
    return urllib2.urlopen(request).read()


def writePage(html,filename):
    """
        作用：将html内容写入本地
        html:服务器相应文件内容
    :param html:
    :return:
    """
    print "【正在保存】" + filename
    with open(filename, "w") as f:
        f.write(html)
    print "-" * 30

def tiebaSpider(url, beginPage,endPage):
    """
    作用：贴吧爬虫调度器
    :return:
    """
    for page in range(beginPage,endPage+1):
        pn = (page -1) * 50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        html = loadPage(fullurl,filename)
        #print html
        writePage(html, filename)
        print "【谢谢使用】"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({
        "kw":kw
    })
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)




# url = "http://tieba.baidu.com/f?kw=%E6%88%98%E7%8B%BC&ie=utf-8&pn=300"
#
# ua_list = [
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
#     "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
#     "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
# ]
#
# user_agent = random.choice(ua_list)
#
# headers = {
#     "User-Agent":user_agent
# }
#
# request = urllib2.Request(url, headers=headers)
#
# response = urllib2.urlopen(request)
#
# print response.read()


