# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/9/17'

"""
https://www.zhihu.com/captcha.gif?r=1502267133738&type=login&lang=cn
{"img_size":[200,44],"input_points":[[20.8,22.7],[41.8,29.7],[57.8,28.7],[87.8,23.7],[113.8,29.7],[141.8,28.7],[159.8,27.7]]}
"""
from bs4 import BeautifulSoup

import requests
import time

def captcha(captcha_data):
    with open("captcha.jpg","wb") as f:
        f.write(captcha_data)
    text = raw_input("请输入图中倒立文字：")
    return text

def zhihuLogin():

    #构建Session对象保存Cookie
    sess = requests.Session()

    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0"
    }

    html=sess.get("https://www.zhihu.com/#signin", headers=headers).text
    bs = BeautifulSoup(html, "lxml")

    _xsrf = bs.find("input", attrs={"name":"_xsrf"}).get("value")

    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn" % (time.time() * 1000)
    #获取图片数据流
    captcha_data = sess.get(captcha_url, headers = headers).content

    #手动输入验证码里的文字
    text = captcha(captcha_data)
    #print captcha_url

    data = {
        "_xsrf" : _xsrf,
        "captcha_type":"cn",
        "password":"***",
        "phone_num":"***",
        "captcha":text
    }

    post_url = "https://www.zhihu.com/login/phone_num"
    response = sess.post(post_url, data=data, headers=headers)
    #print response.text

    response = sess.get("https://www.zhihu.com/people/seal-98-49",headers = headers)
    #print response.text
    with open("my.html","w") as f:
        f.write(response.text.encode("utf-8"))

if __name__ == "__main__":
    zhihuLogin()






