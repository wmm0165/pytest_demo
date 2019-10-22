# -*- coding: utf-8 -*-
# @Time : 2019/10/20 23:01
# @Author : wangmengmeng
import pytest
import smtplib

# 测试代码的执行顺序： yield前的代码-测试用例中的代码-yield后的代码
@pytest.fixture(scope='module')
def smtp_connection():
    smtp_connection = smtplib.SMTP('smtp.126.com',25)
    yield smtp_connection
    print("teardown smtp")
    smtp_connection.close()
