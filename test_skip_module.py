# -*- coding: utf-8 -*-
# @Time : 2019/10/24 23:25
# @Author : wangmengmeng
import pytest


pytestmark = pytest.mark.skip(reason='nopass')   # 无条件跳过整个模块的测试用例
def test_the_unknown():
    assert 1 == 1


def test_module():
    assert 1 == 1
