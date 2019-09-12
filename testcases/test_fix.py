# -*- coding: utf-8 -*-
# @Time : 2019/8/31 14:59
# @Author : wangmengmeng

def test_s7(login_test):
    print("用例1：登录之后其它动作111")


class Test1:
    def test_s1(self, login_test):
        print("用例1：登录之后其它动作111")

    def test_s2(self):  # 不传login
        print("用例2：不需要登录，操作222")

    def test_s3(self, login):
        print("用例3：登录之后其它动作333")


class Test2:
    def test_s4(self, login_test):
        print("用例4：登录之后其它动作444")

    def test_s5(self, login):  # 不传login
        print("用例5：不需要登录，操作555")

    def test_s6(self, login):
        print("用例6：登录之后其它动作666")
