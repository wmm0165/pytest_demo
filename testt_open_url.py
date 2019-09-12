# -*- coding: utf-8 -*-
# @Time : 2019/8/30 11:13
# @Author : wangmengmeng
from selenium import webdriver
import pytest


class TestBaidu:
    def test_open_url(self):
        try:
            driver = webdriver.Chrome()
            driver.get("http://www.baidu.com")
            title = driver.title
            print(driver.title)

            assert title == '百度一下，你就知道'

        except AssertionError:
            raise AssertionError("断言失败！")
        driver.quit()

    def test_baidu(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        title = driver.title
        print(title)


if __name__ == '__main__':
    pytest.main()
