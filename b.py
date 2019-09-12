# -*- coding: utf-8 -*-
# @Time : 2019/8/31 17:30
# @Author : wangmengmeng
a = [i+1 for i in range(5)]  # 列表生成式
print(a)
b = (i+1 for i in range(5))  # 生成器
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
for i in b:
    print(b)
