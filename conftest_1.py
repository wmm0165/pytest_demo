# -*- coding: utf-8 -*-
# @Time : 2019/10/20 18:22
# @Author : wangmengmeng
import pytest
import smtplib


@pytest.fixture()
def smtp_connection():
    return smtplib.SMTP('smtp.126.com',25)
