# -*- coding: utf-8 -*-
# @Time : 2019/9/1 20:46
# @Author : wangmengmeng
import pytest


@pytest.fixture(scope='function')
def login_test():
    print("登录")
