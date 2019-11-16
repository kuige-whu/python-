#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/14
from functools import  reduce

a=[1,3,5]
b=reduce(lambda x,y:x+y,a)
print('1.列表里面整数累加==:',b)
# 1.列表里面整数累加==: 9

a=[[1,3,5],[6]]
b=reduce(lambda x,y:x+y,a)
print('2.列表里面的列表相加—:',b)
# 2.列表里面的列表相加—: [1, 3, 5, 6]

a=[[["abc","123"],["def","456"],["ghi","789"]]]
b=reduce(lambda x,y:x+y , a )
print('列表里面的列表相加—:',b)
# 列表里面的列表相加—: [['abc', '123'], ['def', '456'], ['ghi', '789']]

a=[("abc","123"),("def","456"),("ghi","789")]
b=reduce(lambda x,y:x+y , a )
print('3.列表里面的元组相加!!',b)
# 3.列表里面的元组相加!! ('abc', '123', 'def', '456', 'ghi', '789')

a=['abc','def','hij']
b=reduce(lambda x,y:x+y,a)
print('4.列表里面字符串的累加:~~',b)
# 4.列表里面字符串的累加:~~ abcdefhij

a=('abc','def','hij')
b=reduce(lambda x,y:x+y,a)
print('元祖里面字符串的累加:~~',b)
# 元祖里面字符串的累加:~~ abcdefhij

a=[['abc','def','hij']]
b=reduce(lambda x,y:x+y,a)
print('嵌套列表里面字符串的累加:~~',b)
# 嵌套列表里面字符串的累加:~~ ['abc', 'def', 'hij']


#总结：
#1.functools函数；reduce分解；lambda 匿名函数；x,y:x+y 表达式
#2.使用functools.reduce，要是整数就累加；
#3.使用functools.reduce，要是字符串、列表、元祖就拼接（相当脱了一层外套）