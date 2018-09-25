# -*- coding:gbk -*-

import functools
"'增强now()函数的功能，  " \
"比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，" \
"这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。'"

def log(func):                 #函数运行前，打印日志，再运行
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):                 #函数运行前，打印日志（含参数），再运行
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__，
# Python内置的functools.wraps就是干这个事的。




@log('execute')
@log
def now():
    print ('2013-12-25')
f = now
print(now.__name__)

# print(execute now)