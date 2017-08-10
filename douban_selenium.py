# _*_ coding:utf-8 _*_
__author__ = 'seal'
__data__ = '8/10/17'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path="/Users/seal/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get("https://www.douban.com/")
#driver.save_screenshot("douban.png")

"""
form_email
form_password
captcha_field
"""
driver.find_element_by_id("form_email").send_keys("***")
driver.find_element_by_id("form_password").send_keys("***")
driver.save_screenshot("douban.png")

a=raw_input("请输入验证码")
driver.find_element_by_id("captcha_field").send_keys(a)
driver.find_element_by_class_name("bn-submit").click()
driver.save_screenshot("doubanlogin.png")


