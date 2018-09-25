#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

def build_model(layers):  # LSTM模型。
    model = Sequential()  # Sequential模型，就是多个网络层的线性堆叠
    model.add(LSTM(
        input_shape=(layers[1], layers[0]),  # 二阶张量
        output_dim=layers[1],
        return_sequences=True))  # 布尔值，默认False，控制返回类型。若为True则返回整个序列，否则仅返回输出序列的最后一个输出 。
    model.add(Dropout(0.2))  # 每一次训练时，随机扔掉0.2的结点 。

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers[3]))
    model.add(Activation("linear"))  # LSTM神经网络模型的训练可以通过调整很多参数来优化，
    # 例如activation函数，LSTM层数，输入输出的变量维度等，

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")  # compile 配置学习过程。
    print("> Compilation Time : ", time.time() - start)
    return model



def predict_sequences_multiple(model, data, window_size, prediction_len):
    # Predict sequence of 50 steps before shifting prediction run forward by 50 steps
    prediction_seqs = []
    for i in range(int(len(data) / prediction_len)):
        curr_frame = data[i * prediction_len]
        predicted = []
        for j in range(prediction_len):
            predicted.append(model.predict(curr_frame[newaxis, :, :])[0, 0])
            curr_frame = curr_frame[1:]
            curr_frame = np.insert(curr_frame, [window_size - 1], predicted[-1], axis=0)
        prediction_seqs.append(predicted)
    return prediction_seqs


