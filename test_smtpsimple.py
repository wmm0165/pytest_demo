# -*- coding: utf-8 -*-
# @Time : 2019/10/20 17:52
# @Author : wangmengmeng
import pytest
import smtplib


@pytest.fixture()
def smtp_connection():
    return smtplib.SMTP('smtp.126.com',25)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0
