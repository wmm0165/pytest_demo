# -*- coding: utf-8 -*-
# @Time : 2019/9/4 16:17
# @Author : wangmengmeng
import pytest


@pytest.fixture()
def username():
    name = 'wangmm'
    return name


@pytest.fixture()
def pw():
    password = '123456'
    return password


def test_user(username, pw):
    assert username == 'wangmm'
    assert pw == '123456'
