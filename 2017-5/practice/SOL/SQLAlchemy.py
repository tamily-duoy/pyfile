# -*- coding: utf-8 -*-

#----------------------------------------------
#表的内容用Python的数据结构表示出来的话，
# 可以用一个list表示多行，
# list的每一个元素是tuple，
# 表示一行记录，比如，包含id和name的user表
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
#----------------------------------------------------------
# SQLAlchemy的用法
# 第一步，导入SQLAlchemy，并初始化DBSession
#完成SQLAlchemy的初始化和具体每个表的class定义。

# 导入:
import _mysql
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


#如何向数据库表中添加一行记录
# 创建session对象:
session = DBSession()

# 创建新User对象:
new_user = User(id='5', name='Bob')

# 添加到session:
session.add(new_user)

# 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()
