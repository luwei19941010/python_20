#-*-coding:utf-8-*-
# Author:Lu Wei
#1.简述面向对象三大特性并用代码表示。
'''



#1.封装
#1.1数据封装在对象中 ，方便以后使用
class Foo1(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=Foo1('luwei',10)
print(obj1.name)

class Foo2(object):
    def read(self):
        pass
    def wirte(self):
        pass
obj2=Foo2()
obj2.wirte()
obj2.read()
#1.2继承
class Foo3(object):
    def read(self):
        print('123')
        pass
class Foo4(Foo3):
    def write(self):
        pass
obj3=Foo4()
obj3.read()
#1.3多态
def Foo5(object):
    def func(self,arg):
        arg.send()
        pass
'''
#2.什么是鸭子模型？
#对于一个函数而言，python对参数的类型不会限制，那么传入参数就可以是各种类型，在函数如何列如：arg.send方法，那么就是对于传入类型的一个限制（具备arg.send方法）
#这就是鸭子模型，类似于上述的函数我们认为只要呱呱叫的就是鸭子（只要有send方法，就是我们想要的类型）


#3.列举面向对象中的类成员和对象成员。
#3.1类成员：类变量，绑定方法，静态方法，类方法，属性
#3.2对象成员：对象变量（实例变量)

#4.@methodclass和@staticmethod的区别?
#调用方法:  类.方法(),【对象.方法()不推荐】
#@staticmethod 参数不做限制，@methodclass至少需要传入一个cls【当前类本身】

#5.Python中双下滑 __ 有什么作用？
#私有，只允许内部调用，不允许外部调用

#6.看代码写结果
#这题重点考察实例化对象时 是给对象创建一块空内存地址（因为类中没有__init__) ，对象只能访问类变量不能修改类变量。
# class Base:
#     x = 1
#
#
# obj = Base()
#
# print(obj.x)#1
# obj.y = 123
# print(obj.y)#123
# obj.x = 123
# print(obj.x)#123
# print(Base.x)#1

#7.看代码写结果
# class Parent:
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)#1,1,1
# Child2.x = 2
# print(Parent.x, Child1.x, Child2.x)#1,1,2
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)#1,3,2


#8.看代码写结果
# class Foo(object):
#     n1 = '武沛齐'
#     n2 = '金老板'
#     def __init__(self):
#         self.n1 = '女神'
#
# obj = Foo()
# print(obj.n1)#'女神'
# print(obj.n2)#'金老板'


#9.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#     n1 = '武沛齐'
#     def __init__(self,name):
#         self.n2 = name
# obj = Foo('太白')
# print(obj.n1)#武沛齐
# print(obj.n2)#太白
#
# print(Foo.n1)#武沛齐
# print(Foo.n2)#错误


#10.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num#666
#         self.__salary = 1000
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj = Foo(666)
#
# print(obj.num)#666
# print(obj.a1)#1
# # print(obj.__salary)#不能访问
# # print(obj.__a2)#不能访问
# print(Foo.a1)#1
# # print(Foo.__a2)#不能访问

#11.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#     a1 = 1
#
#     def __init__(self, num):
#         self.num = num
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj1 = Foo(666)
# obj2 = Foo(999)
# print(obj1.num)#666
# print(obj1.a1)#1
#
# obj1.num = 18
# obj1.a1 = 99
#
# print(obj1.num)#18
# print(obj1.a1)#99
#
# print(obj2.a1)#1
# print(obj2.num)#999
# print(obj2.num)#999
# print(Foo.a1)#1
# print(obj1.a1)#99


#12.看代码写结果，注意返回值。
# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run()
# print(v1)
# #f3
# #f2
# #999
# #none


#13.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @staticmethod
#     def f2():
#         print('f2')
#
#
# obj = Foo()
# obj.f1()#f1
# obj.f2()#f2
#
# # Foo.f1()#错误
# Foo.f2()#f2


#14.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#
# obj = Foo()
# obj.f1()#f1
# obj.f2()#f2
#
# # Foo.f1()#cuowu
# Foo.f2()#f2


#15.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#
#     def f1(self):
#         print('f1')
#         self.f2()
#         self.f3()
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#     @staticmethod
#     def f3():
#         print('f3')
#
# obj = Foo()
# obj.f1()
# #f1
# #f2
# #f3


#16.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Base(object):
#     @classmethod
#     def f2(cls):
#           print('f2')
#
#     @staticmethod
#     def f3():
#           print('f3')
#
# class Foo(Base):
#     def f1(self):
#         print('f1')
#         self.f2()
#         self.f3()
#
# obj = Foo()
# obj.f1()
# #f1
# #f2
# #f3

#17.看代码写结果
# class Foo(object):
#     def __init__(self, num):
#         self.num = num
#
#
# v1 = [Foo for i in range(10)]
# v2 = [Foo(5) for i in range(10)]
# v3 = [Foo(i) for i in range(10)]
#
# # print(v1)
# # print(v2[3].num)
# # print(v3[8].num)
# #[Foo,...Foo] 10个类
# #10个Foo(5)对象
# #[Foo(0),Foo(1),Foo(2)...Foo(9)]



#18.看代码写结果
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     print(item.num)
# #1
# #2
# #3



#19.看代码写结果
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)
#     #1.666
#     #2.666
#     #3.666


#20.看代码写结果
# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p3 = Person('安安', 19, d2)
#
# print(p1.name)#武沛齐
# print(p2.age)#18
# print(p3.depart)#d2对象
# print(p3.depart.title)#销售部


#21.看代码写结果

# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message()#我是武沛齐,年龄18,属于人事部
# p2.message()#我是alex,年龄19,属于人事部
#




