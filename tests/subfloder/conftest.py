# -*- coding: utf-8 -*-
# @Time : 2019/10/22 17:42
# @Author : wangmengmeng
import pytest


@pytest.fixture()
def username():
    return 'overridden-' + 'username'