# -*- coding: utf-8 -*-
# @Time : 2019/10/24 23:47
# @Author : wangmengmeng
import pytest
import sys


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
class TestSkipClass:
    def test_function(self):
        "will not be setup or run under 'win32' platform"