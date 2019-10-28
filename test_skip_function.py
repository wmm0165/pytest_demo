# -*- coding: utf-8 -*-
# @Time : 2019/10/24 23:25
# @Author : wangmengmeng
import pytest
import sys


@pytest.mark.skip(reason='no way of currently testing this')
def test_the_unknown():
    assert 1 == 1


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")  # 有条件跳过测试用例
def test_function():
    assert 1 == 1
