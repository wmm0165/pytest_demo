# -*- coding: utf-8 -*-
# @Time : 2019/8/31 14:55
# @Author : wangmengmeng
import pytest


@pytest.fixture(scope="class")
def login():
    print("登录系统")