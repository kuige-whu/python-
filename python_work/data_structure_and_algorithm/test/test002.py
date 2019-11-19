#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/7
import numpy as np

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

a=[1,2,3]
b=[4,5,6]
c=len(a)
print(a)
print(b)
print(c)
a[c:] = b
print(a)
a=np.arange(5)
b=np.arange(5,9,2)
a=range(5)
print(a)
a=[0,1,2,3,4,5,6,7]
print(a)
a.insert(5,435)
print(a)
a.remove(5)
print(a)
a=[1,2,3,4,5,6,717]
print(a.pop(6))
print(a)
a.reverse()
print(a)
a.sort()
print(a)
lst = ["Python", "java", "c", "pascal", "basic"]
lst.sort(key=len)
print(lst)

s = "I am, writing\npython\tbook on line"
print(s)
a=s.split()
print(s)
print(s.split())
print("".join(a))
print(" ".join(a))

# 字典
person = {"name":"qiwsir","site":"qiwsir.github.io","language":"python"}
print(person)
person['name2']="qiwsir"
print(person)
name = (["first","Google"],["second","Yahoo"])
website = dict(name)
print(website)
ad = dict(name="qiwsir", age=42)
print(ad)
website = {}.fromkeys(("third","forth"),"facebook")

# Python 字典 fromkeys() 函数用于创建一个新字典，
# 以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
# dict.fromkeys(seq[, value])
seq = ('Google', 'Runoob', 'Taobao')

dict = dict.fromkeys(seq)
print("新字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" % str(dict))

print(website)
city_code = {"suzhou":"0512", "tangshan":"0315", "beijing":"011", "shanghai":"012"}
# 需要提醒注意的是，在字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型
dd = {(1,2):1}
print(dd)
# dd = {[1, 2]: 1}
print(dd)

# d[key]，返回字典(d)中的键(key)的值
# • d[key]=value，将值(value)赋给字典(d)中的键(key)
# • del d[key]，删除字典(d)的键(key)项（将该键值对删除）
# • key in d，检查字典(d)中是否含有键为 key 的项

# 字符串格式化输出
city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"}
str=" Suzhou is a beautiful city, its area code is %(suzhou)s" % city_code
print(str)
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"qiwsir", "lang":"python"}
print(temp % my)

# 浅拷贝：Python 只存储基本
# 类型的数据，比如 int,str，对于不是基础类型的，比如刚才字典的值是列表，Python 不会在被复制的那个对象
# 中重新存储，而是用引用的方式，指向原来的值。如果读者没有明白这句话的意思，我就只能说点通俗的了（我
# 本来不想说通俗的，装着自己有学问），Python 在所执行的复制动作中，如果是基本类型的数据，就在内存中重
# 新建个窝，如果不是基本类型的，就不新建窝了，而是用标签引用原来的窝。这也好理解，如果比较简单，随便
# 建立新窝简单；但是，如果对象太复杂了，就别费劲了，还是引用一下原来的省事。

# 在 Python 中，有一个“深拷贝”(deep copy)。不过，要用下一 import 来导入一个模块。这个东西
# 后面会讲述，前面也遇到过了。

# 字典赋值即引用
x = {"name": "qiwsir", "lang": ["Python", "java", "c"]}
print()
print(x)
print(id(x))
print(id("name"))
print("浅拷贝，浅层互不干扰，深层为引用")
y = x.copy()
z=x
print(x)
print(y)
print(z)
print(id(x))
print(id(y))
print(id(z))
print("_"*20)
print(id("name"))
print(id(x["name"]))
print(id(y["name"]))
print()
y["lang"].remove('java')
y["name"]= "dkaugkja"
print("y[\"name\"]= \"dkaugkja\"")
print(id(x["name"]))
print(id(y["name"]))
print(id(x["lang"]))
print(id(y["lang"]))
print(x)
print(y)
print(id(x))
y = x.copy()
print(y)
print(id(y))


# key的值必须为常量，不能是非常量a,b,c,d
x={'a': 1, 'b': 2, 'c': 3, 'd': ["e","f"]}
print(id(x))
print(id('a'),id('b'),id('e'))
y=x
print(id(y))
print(id('a'),id('b'),id('e'))
y=x.copy()
print(id(y))
print(id('a'),id('b'),id('e'))


import copy
y=copy.deepcopy(x)





