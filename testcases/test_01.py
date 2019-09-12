# -*- coding: utf-8 -*-
# @Time : 2019/9/4 16:43
# @Author : wangmengmeng
import pytest


@pytest.fixture()
def user():
    print("用户名")
    name = 'wangmm'
    password = '123456'
    return name,password


def test_a(user):
    u = user[0]
    p = user[1]
    assert u == 'wangmm'
