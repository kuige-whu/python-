#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/7 
import numpy as np
a= np.array([[1,2,3],[4,5,6],[7,8,9]])


a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素

x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print (y)

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print  ('这个数组的四个角元素是：')
print (y)

a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(a)
print(b)
print(c)
print(d)

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print  ('大于 5 的元素是：')
print (x[x >  5])

a = np.array([np.nan,  1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])

a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])

x=np.arange(32).reshape((8,4))
print (x[[4,2,1,7]])
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])

x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])

print("广播")
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print (c)

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a + b)

print("横向纵向复制")
mat=[[1,2],[3,4]]
a = np.tile(mat, (1, 4))
print(a)
a = np.tile(mat, 4)
print(a)
a = np.tile(mat, (4,1))
print(a)

print("迭代")
a = np.arange(6).reshape(2,3)
print ('原始数组是：')
print (a)
print ('\n')
print ('迭代输出元素：')
print("a")
for x in np.nditer(a):
    print (x, end=", " )
print ('\n')

print("控制遍历顺序")
a = np.arange(6).reshape(2, 3)
print("a.T")
for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

print("aC")
for x in np.nditer(a.copy(order='C')):
    print(x, end=", ")
print('\n')
print("aTC")
for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")
print('\n')


print("aF")
for x in np.nditer(a.copy(order='F')):
    print(x, end=", ")
print('\n')

print("aTF")
for x in np.nditer(a.T.copy(order='F')):
    print (x, end=", " )
print ('\n')

# for x in np.nditer(a, order='F'): Fortran
# order，即是列序优先；
# for x in np.nditer(a.T, order='C'): C
# order，即是行序优先；

print("显示强制")
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('以 C 风格顺序排序：')
for x in np.nditer(a, order =  'C'):
    print (x, end=", " )
print ('\n')
print ('以 F 风格顺序排序：')
for x in np.nditer(a, order =  'F'):
    print (x, end=", " )

