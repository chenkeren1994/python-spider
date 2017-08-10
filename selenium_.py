# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/9/17'
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="/Users/seal/phantomjs-2.1.1-macosx/bin/phantomjs")

driver.get("http://www.baidu.com/")

from selenium.webdriver.common.keys import Keys
driver.find_element_by_id("kw").send_keys(u"美女")
# driver.save_screenshot("baidu.png")
#print driver.page_source
#print driver.get_cookies()
driver.find_element_by_id("su").send_keys(Keys.RETURN)