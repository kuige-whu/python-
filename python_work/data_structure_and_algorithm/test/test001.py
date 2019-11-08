#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/7
import math

# 取地址函数
s1=id(1)
s2=id(11)
id(3.222222)
id(3.0)
# 取类型函数
type(3)
type(3.0)
type(3.222222)
# +，-，*，/,//, %
# 整除函数
divmod(5,3)
# 取精确位数
round(1.234232,3)
round(4312.32134,-1)
# math函数
math.pi
# 查看函数功能
dir(math)
# 每个函数的使用方法
help(math.pow)
# 在 shell 或者 cmd 中，执行：Python (文件名.py)
str1="hello"
str2= "Hello"
# python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，
# 在交互模式下使用时，需要导入模块。
# cmp(str1,str2)
import operator
operator.eq(str1,str2)
# :比较 2 个序列值是否相同
# 占位符%s，%d，%f
"I like %s" % "python"
s2 = "Suzhou is more than {} years. {} lives in here.".format(2500, "qiwsir")
# 占位符{}
lang = "Python"
print("I love %(program)s"%{"program":lang})


# S.strip() 去掉字符串的左右空格
# S.lstrip() 去掉字符串的左边空格
# S.rstrip() 去掉字符串的右边空格




if  __name__ == "__main__":
    print(s1, s2,  id(3.222222), id(3.0))
    print(type(3), type(3.0), type(3.2222))
    print(type(335578381937218991297937196941))
    print(5/3, 5//3, 5%3)
    print(round(1.234232,3), round(4312.32134,-1))
    print(math.pi)
    print(dir(math))
    print(help(math.pow))
    print(math.pow(2,10))
    print(operator.eq(str1,str2))
    print(ord('1'))
    print(chr(97))
    print("_"*20)

