# -*- coding: utf-8 -*-
# @Time : 2019/10/22 23:28
# @Author : wangmengmeng
import pytest


@pytest.fixture()
def username(username):
    return 'overriden-' + username


def test_username(username):
    assert username == 'overriden-username'