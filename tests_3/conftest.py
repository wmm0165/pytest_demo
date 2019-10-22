# -*- coding: utf-8 -*-
# @Time : 2019/10/23 0:16
# @Author : wangmengmeng
import pytest


@pytest.fixture()
def username():
    return 'username'

@pytest.fixture()
def other_name(username):
    return 'other-' + username