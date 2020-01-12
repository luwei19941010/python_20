### day20

#### 今日内容

- 类成员
- 成员修饰符

#### 1.成员

- 类
  - 类变量（静态字段/属性）
  - 绑定方法
  - 静态方法 @staticmethod
  - 类方法@classmethod
  - 属性@property
- 实例（对象）
  - 实例变量（字段/属性）

##### 1.1实例变量

```
class Foo:
	def __init__(self,name):
		self.name=name
	def info(self):
		pass
obj1=Foo('alex')
obj2=Foo('eric')
```

![image-20200112144521457](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200112144521457.png)

##### 1.2类变量

![image-20200112150128918](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200112150128918.png)

定义：卸载类下一级和方法同级别。

访问：

```
Foo.city
obj1.city
obj2.city
类.类变量名称
对象.类变量名称
```

类变量面试题：

```
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
```



类变量中继承关系

![image-20200112151529111](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200112151529111.png)

```
class Base1:
    x=1
class Foo1(Base1):
    pass

print(Base1.x)#1
print(Foo1.x)#1
Base1.x=66
print(Base1.x)#66
print(Foo1.x)#66
```

总结：找变量优先找自己的，自己没有找类或基类

##### 1.3方法(绑定方法/普通方法)

- 定义：至少有一个self参数
- 执行：先创建对象，由对象.方法

```
class Foo:
	def func(self,a,b):
		print(a,b)
obj=Foo()
obj.func(1,2)
```

##### 1.4静态方法

- 定义：
  - 有装饰器（@staticmethod）
  - 参数：没有参数的限制
- 执行：直接有类.方法。但是python中对象.方法也可以执行静态方法（不推荐）

```
class Foo:
    def __init__(self,name):
        self.name=name

    def func(self, a, b):
        print(self.name,a, b)

    @staticmethod
    def func1():
        print(123)

obj = Foo('luwei')
obj.func(1, 2)

Foo.func1()
obj.func1()#不推荐
```

##### 1.5类方法：

- 定义：
  - 有装饰器（@classmethod）
  - 参数：至少要有一个参数cls（当前类本身）
- 执行：直接有类.方法。但是python中对象.方法也可以执行类方法（不推荐）

```
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
```

面试题：classmethod与staticmethod区别

```
'''
一个是类方法一个是静态方法
定义：
	类方法：使用@classmethod进行装饰，参数至少传一个cls
	静态方法：使用@staticmethod进行装饰，对参数没有限制
调用：
	类.方法直接调用
	对象.方法直接调用
'''
```

##### 1.6属性

- 定义：

  - @property装饰器
  - 只有一个self参数

- 执行：

  - 对象.方法   不加括号

    

```
class Foo:

    @property
    def func(self):
        print('123')
        return 666

obj=Foo()
result=obj.func
print(result)
```



#### 2.成员修饰符

- 公有 私有地方都能访问

- 私有 只有自己能访问到。派生类也访问不了

  - 只有内部能访问，外部访问不了。

  ```
  #实例变量私有
  class Foo:
  
      def __init__(self,name):
          self.__name=name
  
      def func(self):
          print(self.__name)@内部访问
  
  obj=Foo('luwei')
  # print(obj.__name)#私有 报错，外部访问不了
  obj.func()
  ```

  ```
  #类变量私有
  class Foo:
      __x=123
      def __init__(self,name):
          self.__name=name
      @staticmethod
      def func():
          print(Foo.__x)#内部访问
  
  obj=Foo('luwei')
  # print(Foo.__x)#私有 报错，外部访问不了
  Foo.func()
  ```

  ```
  #方法私有
  class Foo:
      def  __func(self):
          print('msg')
  
      def show(self):
          self.__func()#内部访问
  obj=Foo()
  # obj.__func()#私有 报错，外部访问不了
  obj.show()
  ```

  ```
  #继承派生类也无法访问私有
  class Foo:
      def  __func(self):
          print('msg')
  
  class Foo1(Foo):
      def func(self):
          print('Foo1')
          self.__func()#私有 报错，派生类访问不了
          
  obj=Foo1()
  obj.func()#私有 报错，外部访问不了
  ```

  强制访问

  ```
  class Foo:
  
      def __init__(self,name):
          self.__name=name
         
   obj=Foo('luwei')
  print( obj._Foo__name)####强制访问
  ```


新式类

```
# 在python3中这俩的写法是一样，因为所有的类默认都会继承object类，全部都是新式类。
1.class Foo:
	pass

2.class Foo(object):
	pass

#python2中1为经典类，2为新式类
```

 