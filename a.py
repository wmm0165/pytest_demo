# -*- coding: utf-8 -*-
# @Time : 2019/8/31 15:22
# @Author : wangmengmeng

def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
a =fib(6)
print(a)
for i in fib(6):
   print(i)