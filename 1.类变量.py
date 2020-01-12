
#-*-coding:utf-8-*-
# Author:Lu Wei



class Foo:
    city='hangzhou'
    def __init__(self,name):
        self.name=name
    def func(self):
        pass


obj1=Foo('luwei')

print(obj1.city)#先去对象中找，没有再去类中找
obj1.x=123#在对象中添加一个x=123的变量
print(obj1.x)
obj1.city='beijin'
print(obj1.city)
print(Foo.city)



class Base1:
    x=1
class Foo1(Base1):
    pass

print(Base1.x)
print(Foo1.x)
Base1.x=66
print(Base1.x)
print(Foo1.x)