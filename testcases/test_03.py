# -*- coding: utf-8 -*-
# @Time : 2019/9/4 17:07
# @Author : wangmengmeng
import pytest

@pytest.fixture()
def first():
    a = "wangmm"
    return a

@pytest.fixture()
def sencond(first):
    '''psw调用user fixture'''
    a = first
    b = "123456"
    return (a, b)

def test_1(sencond):
    '''用例传fixture'''
    assert sencond[0] == "wangmm"
    assert sencond[1] == "123456"