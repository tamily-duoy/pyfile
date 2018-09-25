#!/usr/bin/python
# -*- coding:utf-8 -*-
import netCDF4 as nc
import shapefile
import matplotlib.pyplot as plt
nc_obj1=nc.Dataset("C:\\Users\\Administrator\\Desktop\\precip.2015 - 2.nc")
nc_obj=nc.Dataset("C:\\Users\\Administrator\\Desktop\\precip.mon.mean.nc")

print("文件中有:")
print(nc_obj)   #看看NC文件中有甚麼么
print("文件中的变量:")
print(nc_obj.variables.keys())  #查看nc文件中的变量

print("precip 变量：")
print(nc_obj.variables['precip']) #查看U這個变量
print("precip 变量的属性")
print(nc_obj.variables['precip'].ncattrs()) #属性
print("precip 变量的units属性的单位")
print(nc_obj.variables['precip'].dataset)   #查看U的其中一個属性[单位]
#<span style="background-color: rgb(240, 240, 240);">讀取U的數據值</span>
# UU=nc_obj.variables['lat'][:30]  #读取lat的数据值
print("====")
# print(nc_obj.variables['lat'].ncattrs())





