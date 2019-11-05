# -*- coding: utf-8 -*-
# @Time : 2019/11/6 0:03
# @Author : wangmengmeng
import pytest


# def test_aa():
#     assert 1 == 1
#     assert 2 == 2
#     print("ceshi")


def test_bb():
    pytest.assume(1==1)
    pytest.assume(2==3)
    print("测试")
    pytest.assume(3 == 3)

# https://www.jianshu.com/p/7df6d781f100