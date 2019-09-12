# -*- coding: utf-8 -*-
# @Time : 2019/9/10 11:41
# @Author : wangmengmeng

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_link_text("新闻").click()
print(driver.current_url)
# driver.find_element(By.CSS_SELECTOR,".btn_wr>input").click()
# driver.find_element("css selector",".btn_wr>input").click()
# driver.find_element_by_css_selector(".btn_wr>input").click()
time.sleep(2)
driver.quit()
