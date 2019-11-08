#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/8 
import numpy as np

a=np.array([1,2,3])
print(a)
a=np.array([[1,2],[3,4]])
print(a)
a=np.array([1,2,3,4,5,],ndmin=2)
print(a)
a=np.array([1,2,3],dtype=complex)
print(a)

a=np.arange(24)
print(a.ndim)
a=a.reshape(2,4,3)
print(a.ndim)
print(a.shape)
print(a)
a.shape=(2,3,4)
print(a)

x=[1,2,3]
a=np.asarray(x)
print(a)
a=np.array(x)
print(a)
x=[(1,2,3),(4,5)]
a=np.asarray(x)
print(a)
a=np.arange(5)
print(a)
a=np.linspace(1,10,19,endpoint=True, retstep= False)
print(a)
a=np.logspace(1,10,10,base=2,dtype=int)
print(a)
a=np.arange(32)
s=slice(2,21,3)
print(a[s])
print(a[2:21:3])
a=np.arange(9).reshape(3,3)
print(a)
print(a[1:])
print(a[:1])
print(a[...,1])
print(a[1:,...])
a=np.arange(12).reshape(4,3)
print(a)
r=np.array([[0,0],[3,3]])
c=np.array([[0,2],[0,2]])
print(a[r,c])
print(a[...])
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)
print(a|a>6)
print(a[a>6])
a=np.array([1, 2+3j,4,5+6j])
print(a[np.iscomplex(a)])
a=np.arange(32).reshape(8,4)
print(a[[1,3,5,7]])
print(a[np.ix_([1,3],[2,1])])