# -*- coding: utf-8 -*-
# @Time : 2019/10/19 0:40
# @Author : wangmengmeng
import pytest


@pytest.mark.parametrize("x",[0, 1])
@pytest.mark.parametrize("y",[2, 3])
def test_foo(x, y):
    pass