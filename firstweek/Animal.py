#!/usr/bin/env python3

class Animal(object):
    def __init__(self,name):  # 初始化设置名字
        self._name = name   #设置为私有属性
    def get_name(self):      #获取名字，私有属性不可直接被访问
        return self._name
    def set_name(self,value): # 设置私有属性值
        self._name = value
    def make_sound(self):
        pass
