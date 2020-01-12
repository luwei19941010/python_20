# -*-coding:utf-8-*-
# Author:Lu Wei


class Foo:
    def __init__(self,name):
        self.name=name
#绑定方法
    def func(self, a, b):
        print(self.name,a, b)
#静态方法
    @staticmethod
    def func1():
        print(123)
#类方法
    @classmethod
    def func2(cls,a,b):
        print(cls)
        print(a,b)
obj = Foo('luwei')
obj.func(1, 2)
Foo.func1()
obj.func1()
Foo.func2(1,2)
obj.func2(2,3)
