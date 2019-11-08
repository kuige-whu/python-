#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/8
import numpy as np


print("修改数组对象的值，默认readonly，改为writeonly，或者writeonly")
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

print("flags参数")

a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('修改后的数组是：')
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
   print (x, end=", " )

print("广播迭代")
a = np.arange(0,60,5)
a = a.reshape(3,4)
print  ('第一个数组为：')
print (a)
print  ('\n')
print ('第二个数组为：')
b = np.array([1,  2,  3,  4], dtype =  int)
print (b)
print ('\n')
print ('修改后的数组为：')
for x,y in np.nditer([a,b]):
    print ("%d:%d"  %  (x,y), end=", " )

print("改变数组形状")
a = np.arange(8)
print('原始数组：')
print(a)
print('\n')

b = a.reshape(4, 2)
print('修改后的数组：')
print(b)

print("迭代器np.arr.flat")
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)

print("ndarray.flatten(order='C')")
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))

a = np.arange(12).reshape(3, 4)

print("np.transpose()")
print('原数组：')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))

print ('转置数组：')
print (a.T)

# numpy.rollaxis(arr, axis, start)
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 将轴 2 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2))
# 将轴 0 滚动到轴 1：（宽度到高度）
print('\n')

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2, 1))


# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)


print('原数组：')
print(a)
print('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）

print('调用 swapaxes 函数后的数组：')
print(np.swapaxes(a, 2, 0))


