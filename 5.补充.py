# -*-coding:utf-8-*-
# Author:Lu Wei

'''
class Foo:
    def __init__(self, num):
        self.num = num

cls_list = []
for i in range(10):
    cls_list.append(Foo)

for i in range(len(cls_list)):
    obj = cls_list[i](i)
    print(obj.num)


class Foo:
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
obj = Foo()
v = [ obj.f1,obj.f2 ]
for item in v:
    item()


class Foo:
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
    def f3(self):
        v = [self.f1 , self.f2 ]
        for item in v:
            item()
obj = Foo()
obj.f3()


'''

