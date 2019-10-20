# -*- coding: utf-8 -*-
# @Time : 2019/10/20 20:32
# @Author : wangmengmeng


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    # assert 0


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    # assert 0
