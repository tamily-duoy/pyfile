# -*- coding:gbk -*-

import functools
"'��ǿnow()�����Ĺ��ܣ�  " \
"���磬�ں�������ǰ���Զ���ӡ��־�����ֲ�ϣ���޸�now()�����Ķ��壬" \
"�����ڴ��������ڼ䶯̬���ӹ��ܵķ�ʽ����֮Ϊ��װ��������Decorator����'"

def log(func):                 #��������ǰ����ӡ��־��������
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):                 #��������ǰ����ӡ��־������������������
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#��Ϊ���ص��Ǹ�wrapper()�������־���'wrapper'��
# ���ԣ���Ҫ��ԭʼ������__name__�����Ը��Ƶ�wrapper()�����У�
# ������Щ��������ǩ���Ĵ���ִ�оͻ����

# ����Ҫ��дwrapper.__name__ = func.__name__��
# Python���õ�functools.wraps���Ǹ�����µġ�




@log('execute')
@log
def now():
    print ('2013-12-25')
f = now
print(now.__name__)

# print(execute now)