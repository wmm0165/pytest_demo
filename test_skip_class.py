# -*- coding: utf-8 -*-
# @Time : 2019/10/24 23:47
# @Author : wangmengmeng
import pytest
import sys


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.6 or higher")
class TestSkipClass:
    def test_class(self):
        "requires python3.6 or higher"