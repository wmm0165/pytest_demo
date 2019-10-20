# -*- coding: utf-8 -*-
# @Time : 2019/10/20 11:47
# @Author : wangmengmeng
import pytest


@pytest.fixture
def aa():
    print("测试demo")

def test_aa():
    assert 1 == 1