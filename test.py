# -*- coding: utf-8 -*-
# @Time : 2019/8/30 16:37
# @Author : wangmengmeng
# 列表生成式
"""
将已知列表里的每个值增加1
"""
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a  = [i+1 for i in range(10)]
print(a)