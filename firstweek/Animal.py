#!/usr/bin/env python3

class Animal(object):
    def __init__(self,name):  # ��ʼ����������
        self._name = name   #����Ϊ˽������
    def get_name(self):      #��ȡ���֣�˽�����Բ���ֱ�ӱ�����
        return self._name
    def set_name(self,value): # ����˽������ֵ
        self._name = value
    def make_sound(self):
        pass
