# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/10/17'

"""
标题 <h3 class=ellipsis/>
主播 <span class="dy-name ellipsis fl">斗魚丶小可</span>
观看人数 <span class="dy-num fr"></span>
<a class="shark-pager-next" href="#">下一页</a>
<a class="shark-pager-next shark-pager-disable shark-pager-disable-next" href="#">下一页</a>
"""

import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

class douyu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path="/Users/seal/phantomjs-2.1.1-macosx/bin/phantomjs")
        self.num = 0
        self.count = 0

    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup = bs(self.driver.page_source, "lxml")

            names = soup.find_all("h3",{"class":"ellipsis"})
            authors = soup.find_all("span",{"class":"dy-name ellipsis fl"})
            numbers = soup.find_all("span",{"class":"dy-num fr"})

            for name, author, number in zip(names, authors, numbers):
                print u"观众人数：" + number.get_text().strip() + u"\t\t\t\t\t\t主播：" + author.get_text().strip() + u"\t\t\t\t\t\t房间名："+name.get_text().strip()
                self.num += 1
                m = re.search(r'\d+', number.get_text().strip())
                numeric = m.group()
                self.count += int(numeric)

            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

            self.driver.find_element_by_class_name("shark-pager-next").click()

    def tearDown(self):
        print u"当前网站直播人数: " + str(self.num)
        print u"当前网站观众人数：" + str(self.count)

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

