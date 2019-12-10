# -*- coding: utf-8 -*-
# @Time : 2019/11/7 14:09
# @Author : wangmengmeng
import unittest
import os
import sys

prj_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(prj_path)
testcase_path = os.path.join(prj_path, 'test_code')
report_file = os.path.join(prj_path, 'Jenkins_report', 'report.html')
suite = unittest.defaultTestLoader.discover(testcase_path)
with open(report_file, 'wb') as f:
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="wangmengmeng").run(suite)