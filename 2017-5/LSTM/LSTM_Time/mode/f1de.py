#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # tensorflow设置log等级   #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")  # 忽略了警告错误的输出     #Hide messy Numpy warnings

# def reshape_dataset(train): #reshape input to be [samples, time steps, features]
#     trainX = np.reshape(train, (7*train.shape[0], 1, train.shape[1]))
#     return trainX
def loaddata(path,seq_len):
    f = open(path, encoding='utf-8')
    # f = np.loadtxt(path, delimiter=' ', dtype=str,encoding='gb18030',errors='ignore')
    listkey = [] ;result=[]
    for line in f:
        line = line.strip().split(',')
        listkey.append(line)
    # print(listkey)

    sequence_length = seq_len + 1
    for index in range(len(listkey)-sequence_length):
        result.extend(listkey[index:index+sequence_length])
    # print("=================")
    # print(result)
    result=np.array(result)
    result=result[:,:-1]
    # print(result)
    # print('======================')
    # print(result)
    # print("===========")
    row=round(0.7*result.shape[0])
    train=result[:int(row)]

    # testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))



    x_train = train[1:,1:3]
    # x_train = reshape_dataset(x_train)
    # dict([x_train])
    # print(x_train)
    # print(x_train.shape[1])
    # x_train=np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
    # print(x_train)

    x_test = result[int(row):,1:3]
    # x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))
    # print(x_test)
    y_train = train[1:,1:2]
    # y_train = np.reshape(y_train, (y_train.shape[0], 1, y_train.shape[1]))
    # print(y_train)

    y_test = result[int(row):,1:2]
    # y_test = np.reshape(y_test, (y_test.shape[0], 1, y_test.shape[1]))
    return x_train, y_train    # , x_test, y_test
if __name__=='__main__':
    path = '17天气d.txt'
    loaddata(path, 2)
