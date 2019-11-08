#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/7 

# 分割与连接
a = "I LOVE PYTHON"
b=a.split(" ")
c=" ".join(b)
print(a == c,c)

# encode 和 decode
a = "中"
print(a)
print(type(a))
print(len(a))
a=['2',3,'qiwsir.github.io']
print(type(a))
print(len(a))
print(a)
print(a[2:3])
print(a[-2])
print("_"*20)
a = "123456"
print(a[0:4])
print(a[-1])
print(a[:-1])
print(a[-4:-1])
print(a[4:-1])
print("_"*20)

print(a[::1])
print(a[::-1])
print(a[4::-1])
print(a[5:0:-1])
print("_"*20)

print(list((reversed(a))))
print("".join(list((reversed(a)))))
print(a.split(" "))
print(list(a))


a = [1,2,3,4,5,6]
b = [7,8,9,0]
a.extend(b)
print(a)

a=[1,2,3]
b=[4,5,6]
a.append(b)
print(a)
print(a[3])
print(a[3][1:])
print("_"*20,  5)





