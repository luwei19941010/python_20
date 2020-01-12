# -*-coding:utf-8-*-
# Author:Lu Wei
'''
class Foo:

    @property
    def func(self):
        print('123')
        return 666


obj = Foo()
result = obj.func
print(result)
'''

class Page(object):
    def __init__(self, total_count, current_page, per_page_count=10):
        self.total_count=total_count
        self.current_page=current_page
        self.per_page_count=per_page_count

    @property
    def start_index(self):
        return (self.current_page-1)*self.per_page_count

    @property
    def end_index(self):
        return self.current_page*self.per_page_count


user_data=[]
for i in range(131):
    user_data.append('luwei&*&@%s'%(i,))


current_page=int(input('请输入要查看的页码：'))
p = Page(321, current_page)
data_list=user_data[p.start_index:p.end_index]
for i in data_list:
    print(i)