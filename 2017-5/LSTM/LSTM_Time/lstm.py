#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
import warnings
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
import matplotlib.pyplot as plt
from keras.layers.recurrent import LSTM
from keras.models import Sequential

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   #tensorflow设置log等级   #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")           #忽略了警告错误的输出     #Hide messy Numpy warnings
#在tensorflow的log日志等级如下：
# - 0：显示所有日志（默认等级）
# - 1：显示info、warning和error日志
# - 2：显示warning和error信息
# - 3：显示error日志信息

def load_data(filename, seq_len, normalise_window):
    f = open(filename, 'rb').read()
    data = f.decode().split('\n')

    sequence_length = seq_len + 1
    result = []
    for index in range(len(data) - sequence_length):    #生成result数据 。
        result.append(data[index: index + sequence_length])
    
    if normalise_window:    #正则化result 。
        result = normalise_windows(result)

    result = np.array(result)

    row = round(0.9 * result.shape[0])     #精度控制，四舍五入。
    train = result[:int(row), :]        #生成训练数据 。
    np.random.shuffle(train)
    x_train = train[:, :-1]
    y_train = train[:, -1]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, -1]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))  

    return [x_train, y_train, x_test, y_test]

def normalise_windows(window_data):     #正则化result数据 。
    normalised_data = []
    for window in window_data:
        normalised_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalised_data.append(normalised_window)
    return normalised_data

def build_model(layers):   #LSTM模型。
    model = Sequential()   #Sequential模型，就是多个网络层的线性堆叠
          #建立模型有两种方式：一是向layer添加list的方式，二是通过.add()方式一层层添加（一个add为一层），
#keras中，数据是以张量的形式表示的，张量的形状就是shape
    model.add(LSTM(
        input_shape=(layers[1], layers[0]), #二阶张量
        output_dim=layers[1],
        return_sequences=True))   #布尔值，默认False，控制返回类型。若为True则返回整个序列，否则仅返回输出序列的最后一个输出 。
    model.add(Dropout(0.2))    #每一次训练时，随机扔掉0.2的结点 。

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers[3]))
    model.add(Activation("linear"))  #LSTM神经网络模型的训练可以通过调整很多参数来优化，
    # 例如activation函数，LSTM层数，输入输出的变量维度等，

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")  #compile 配置学习过程。
               #优化器optimizer：已预定义的优化器名，如rmsprop、adagrad，或一个Optimizer类的对象 。
     #指标列表metrics：对分类问题，我们一般将该列表设置为metrics=['accuracy']。
        # 指标可以是一个预定义指标的名字，也可以是一个用户定制的函数。
          # 指标函数应该返回单个张量，或一个完成metric_name - > metric_value映射的字典。
    print("> Compilation Time : ", time.time() - start)
    return model

# def predict_point_by_point(model, data):
#     #Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
#     predicted = model.predict(data)
#     predicted = np.reshape(predicted, (predicted.size,))
#     return predicted
#
# def predict_sequence_full(model, data, window_size):
#     #Shift the window by 1 new prediction each time, re-run predictions on new window
#     curr_frame = data[0]
#     predicted = []
#     for i in range(len(data)):
#         predicted.append(model.predict(curr_frame[newaxis,:,:])[0,0])
#         curr_frame = curr_frame[1:]
#         curr_frame = np.insert(curr_frame, [window_size-1], predicted[-1], axis=0)
#     return predicted

def predict_sequences_multiple(model, data, window_size, prediction_len):
    #Predict sequence of 50 steps before shifting prediction run forward by 50 steps
    prediction_seqs = []
    for i in range(int(len(data)/prediction_len)):
        curr_frame = data[i*prediction_len]
        predicted = []
        for j in range(prediction_len):
            predicted.append(model.predict(curr_frame[newaxis,:,:])[0,0])
            curr_frame = curr_frame[1:]
            curr_frame = np.insert(curr_frame, [window_size-1], predicted[-1], axis=0)
        prediction_seqs.append(predicted)
    return prediction_seqs




if __name__=='__main__':
    global_start_time = time.time()
    seq_len = 50
    X_train, y_train, X_test, y_test = load_data('sp501.csv', seq_len, True)

