#!/usr/bin/python
# -*- coding:utf-8 -*-

import shapefile

sf = shapefile.Reader("C:\\Users\\Administrator\\Desktop\\spark\\数据集\\gtwo\\gtwo_areas_201608062356.shp")
shapes = sf.shapes()  # Geometry
print (shapes[1].parts)
# print ( shapes[1].points)
print (len(shapes)) #..条记录

#print len(list(sf.iterShapes())) #..条记录
#for name in dir(shapes[3]): #不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
 #       if not name.startswith('__'):
 #           print  name


# print (sf.numRecords)
recds = sf.records()
print(recds)
print( len(recds))
for i in range(sf.numRecords):
    rcd = sf.record(i)
    #sp = rcd.shape 没有shape属性
    #print sp.points
# recds.shape
# 读取记录
# print (sf.shapeRecord(1).shape.shapeType)
print (sf.shapeRecord(1).record)
print (sf.fields)


# print ''
for shp in range(len(shapes)):
    shap = shapes[shp]
    # print (shap.points)
    # print (shap.shapeType)
    # print (len(shap.points))
    # for i in range(len(shap.points)):
    #     print (shap.points[i])
    #     for x in range(len(shap.points[i])):
    #         print (shap.points[i][x])