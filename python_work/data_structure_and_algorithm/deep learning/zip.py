#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/16


# 注：zip函数返回值是地址
a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
zi = list(zip(a,b))
# 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
zip(a,c)
print(zi)
print(list(zi))
#               # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
print(zip(*zi))
print(list(zip(*zi)))
#           # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]


# 来自 <https://www.runoob.com/python/python-func-zip.html>

# 列表元素依次相连：

# -*- coding: UTF-8 -*-


l = ['a', 'b', 'c', 'd', 'e','f']
print(l)


#打印列表
print (list(zip(l[:-1],l[1:])))

nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)