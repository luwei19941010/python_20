#-*-coding:utf-8-*-
# Author:Lu Wei
"""
编写类完成以下的嵌套关系


角色：学校、课程、班级
要求：
	1. 创建北京、上海、深圳三所学校。
	2. 创建课程
		北京有三种课程：Linux、Python、Go
		上海有两种课程：Linux、Python
		深圳有一种课程：Python
	3. 创建班级(班级包含：班级名称、开班时间、结课时间、班级人数)
		北京Python开设：21期、22期
		北京Linux开设：2期、3期
		北京Go开设：1期、2期
		上海Python开设：1期、2期
		上海Linux开设：2期
		深圳Python开设：1期、2期
"""
class School:
    def __init__(self,schoolname):
        self.schoolname=schoolname

class Course:
    def __init__(self,coursename):
        self.coursename=coursename

class Class:
    def __init__(self,classname,starttime,endtime,num):
        self.classname=classname
        self.starttime=starttime
        self.endtime=endtime
        self.num=num

    def msg(self,school,course):
        self.school=school
        self.course=course
        data='%s开设%s课程%s班级，时间周期%s至%s,人数%s'%(self.school.schoolname, self.course.coursename,self.classname,self.starttime,self.endtime,self.num)
        print(data)



s1=School('北京')
s2=School('上海')
s3=School('深圳')

co1=Course('Linux')
co2=Course('Python')
co3=Course('Go')

cla1=Class('1期','6月','7月',50)
cla2=Class('2期','6月','8月',52)
cla3=Class('3期','6月','9月',53)
cla21=Class('21期','6月','10月',21)
cla22=Class('22期','6月','11月',22)

cla1.msg(s1,co1)
