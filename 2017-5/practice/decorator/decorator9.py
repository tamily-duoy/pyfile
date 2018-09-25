# # -*- coding: utf-8 -*-
"'定义装饰器decorator'"

#------------------------------------------
'''示例1: 最简单的函数,调用了两次
=========运行到f(3)，再调用f(x)函数得到结果'''

def f(x):

    print("f(x) called.")

f(3)
f(4)
#-------------------------------------------------------------
'''示例2: 使用装饰函数在函数执行前和执行后分别附加额外功能
替换函数(装饰)
装饰器参数是（被装饰的）函数（对象），
返回原函数（对象）
装饰的实质语句: f = deco(f)'''

def deco(f):
    print("before f() called.")          #函数执行前，添加的功能
    f()                                    #调用函数
    print("  after f() called.")        #调用函数后，即函数执行后，执行的功能
    return f                   #返回定义的函数，调用装饰器时，返回。

def f():
    print(" f() called.")

f = deco(f)           #装饰的语句====把装饰器和函数连接起来的接口。

f()
f()
#--------------------------------------------------------------------------------
'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''

def deco(f):
    print("before f() called.")
    f()
    print("  after f() called.")
    return f

@deco      #相当于myfunc = deco(myfunc)，给下面定义的函数添加装饰器功能
def f():
    print(" f() called.")

f()
f()
#-------------------------------------------------------------------------------
'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''

def deco(f):
    def _deco():
        print("before f() called.")
        f()
        print("  after f() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco
def f():
    print(" f() called.")
    return 'ok'

f()
f()
#---------------------------------------------------------------------------
'''示例5: 对带参数的函数进行装饰，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''

def deco(f):
    def _deco(a, b):
        print("before f() called.")
        ret = f(a, b)
        print("  after f() called. result: %s" % ret)   # "....:%s" % 数据=====打印数据结果的格式
        return ret
    return _deco

@deco
def f(a, b):
    print(" f(%s,%s) called." % (a, b))
    return a + b

f(1, 2)
f(3, 4)

#-----------------------------------------------------------------------------
# -*- coding:gbk -*-
'''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''

def deco(func):
    def _deco(*args, **kwargs):            #元组 ，字典
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)
#-------------------------------------------------------------------------------
# -*- coding:gbk -*-
'''示例7: 在示例4的基础上，让装饰器带参数，
和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''

def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")             #装饰器带参数
def myfunc():
    print(" myfunc() called.")

@deco("module2")
def myfunc2():
    print(" myfunc2() called.")

myfunc()
myfunc2()
#------------------------------------------------------------------------
# '''示例8: 装饰器带类参数
   #装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器'''


class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")


def deco(cls):
    '''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()

        return __deco

    return _deco
#-----------------------------------------------------------------------------
'''mylocker.py: 公共类 for 示例9.py'''


class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco


# -*- coding:gbk -*-
'''示例9: 装饰器带类参数，并分拆公共类到其他py文件中
同时演示了对一个函数应用多个装饰器'''

from practice.decorator.mylocker import *


class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b


if __name__ == "__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))