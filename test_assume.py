# -*- coding: utf-8 -*-
# @Time : 2019/11/6 0:03
# @Author : wangmengmeng
import pytest
from pytest_assume.plugin import assume
"""
需要安装第三方插件 pytest-assume，插件下载地址:https://files.pythonhosted.org/packages/89/f2/bdb104e65911ad5dd9a32cff0aa4ed29a64f9cbd6e56da988de3c0695b6d/pytest_assume-2.2.0-py3-none-any.whl ,
下载完成后在cmd下进入到下载文件所在目录执行pip install pytest_assume-2.2.0-py3-none-any.whl
"""


# def test_aa():
#     assert 1 == 1
#     assert 2 == 2
#     print("ceshi")


# def test_bb():
#     assume(1 == 1)
#     assume(2 == 3)
#     print("测试")
#     assume(3 == 3)

def test_bb():
    pytest.assume(1 == 1)
    pytest.assume(2 == 3)
    print("测试")
    pytest.assume(3 == 3)