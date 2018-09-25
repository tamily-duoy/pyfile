#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'mayi'

#导入模块
from dbfread import DBF

#数据表文件名
table = DBF("C:\\Users\\Administrator\\Desktop\\spark\\数据集\\gtwo\\gtwo_points_201608062356.dbf")

#遍历数据表中（没加删除标志）的记录
for record in table:
    for field in record:
        print(field, "=", record[field], end = ",")
    print()

print("*" * 40)

#遍历数据表中（加了删除标志）的记录
for record in table.deleted:
    for field in record:
        print(field, "=", record[field], end = ",")
    print()