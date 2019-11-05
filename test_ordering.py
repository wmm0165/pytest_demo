# -*- coding: utf-8 -*-
# @Time : 2019/11/6 0:41
# @Author : wangmengmeng
import pytest


# def test_01():
#     print("one")
#     assert True
#
#
# def test_02():
#     print("two")
#     assert True
@pytest.mark.run(order=2)
def test_01():
    print("one")
    assert True


@pytest.mark.run(order=1)
def test_02():
    print("two")
    assert True
