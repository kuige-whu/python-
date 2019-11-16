#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/15


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性
        self.__number = 0

    # 获取私有属性值  number = p1.number 会执行这个函数
    @property
    def number(self):
        # 返回私有属性值
        return self.__number

    # 设置私有属性值  p1.number = 666
    @number.setter
    def number(self, value):
        # 设置__number的值
        self.__number = value

    # 删除私有属性  del p1.number 会执行这个函数
    @number.deleter
    def number(self):
        # 删除属性
        del self.__number


p1 = People('张三', 22)
# 正常的对象属性赋值
# 对象.属性名 = 属性值
p1.name = '李四'
# 获取对象的属性值
name = p1.name
# 删除对象的属性
del p1.name
# 私有属性升级版
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
num = p1.number
print(num)
# 会去执行@number.setter装饰的number函数，在函数中设置__number属性的值
p1.number = 666
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
print(p1.number)
# 会去执行@number.deleter装饰的number函数，在函数中会将__number属性删除
del p1.number
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
print(p1.number)


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
del obj.price     # 删除商品原价
