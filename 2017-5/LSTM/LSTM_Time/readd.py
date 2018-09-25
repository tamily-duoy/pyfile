#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import warnings
import numpy as np
from sklearn.cross_validation import train_test_split

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # tensorflow设置log等级   #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")  # 忽略了警告错误的输出     #Hide messy Numpy warnings

def readdata(path):
    # path='F:\\pycharm\\pyfile\\2017-5\\spark00\\数据\\17天气de.txt'
    # f = open(path, 'r', encoding='utf-8')
    f = open(path,encoding='utf-8')
    listkey=[]
    for line in f:
        line = line.strip().split(',')
        listkey.append(line)
    f.close()
    return listkey


def loaddata(listkey,seq_len):
    sequence_length = seq_len + 1
    result=[]
    for index in range(len(listkey)-sequence_length):
        result.append(listkey[index:index+sequence_length])
    # print(result)
    result=np.array(result)
    # print(result)
    row=round(0.7*result.shape[0])
    train=result[:int(row),:]

    x_train = train[:, :-1]
    x_test = result[int(row):, :-1]

    y_train = train[:, -1]
    y_test = result[int(row):, -1]
    # x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]))  #shape[0] (行)该维度。[1]列
    # x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return x_train, y_train, x_test, y_test



if __name__=='__main__':
    path = 'F:\\pycharm\\pyfile\\2017-5\\spark00\\数据\\17天气de.txt'
    listkey=readdata(path)
    # print(listkey)
    # listkey=[['\ufeff日期', '最高气温', '最低气温', '天气', '风向', '风力', ''], ['2017-01-01', '24', '13', '晴', '西南风', '1级', ''], ['2017-01-02', '25', '15', '多云', '东北风', '微风', '']]
    c=loaddata(listkey, 3)
    print(c)