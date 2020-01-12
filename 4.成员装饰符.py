#-*-coding:utf-8-*-
# Author:Lu Wei
# class Foo:
#
#     def __init__(self,name):
#         self.__name=name
#
#     def func(self):
#         print(self.__name)
#
# obj=Foo('luwei')
# # print(obj.__name)
# obj.func()
#
# class Foo:
#     __x=123
#     def __init__(self,name):
#         self.__name=name
#     @staticmethod
#     def func():
#         print(Foo.__x)
#
# obj=Foo('luwei')
# # print(Foo.__x)
# Foo.func()
#
#
# # print(obj.__name)


# class Foo:
#     def  __func(self):
#         print('msg')
#
#     def show(self):
#         self.__func()
# obj=Foo()
# # obj.__func()
# obj.show()

class Foo:
    def  __func(self):
        print('msg')

class Foo1(Foo):
    def func(self):
        print('Foo1')
        self.__func()

obj=Foo1()
obj.func()