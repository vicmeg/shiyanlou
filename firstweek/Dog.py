#!/usr/bin/env python3

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Dog: {}'.format(self.name)

dog = Dog('wangcai',2)
print(dog)
print(dog.name)
print(dog.age)
