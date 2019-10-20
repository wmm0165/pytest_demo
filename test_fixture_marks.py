# -*- coding: utf-8 -*-
# @Time : 2019/10/20 23:58
# @Author : wangmengmeng
import pytest


# 使用mark标记 带参数的fixture 中的某些参数枚举值s
@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass
