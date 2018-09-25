#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
import warnings
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # tensorflow设置log等级   #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")  # 忽略了警告错误的输出     #Hide messy Numpy warnings







def load_data(filename, seq_len, normalise_window):
    f = open(filename, 'rb').read()
    data = f.decode().split('\n')

    sequence_length = seq_len + 1
    result = []
    for index in range(len(data) - sequence_length):  # 生成result数据 。
        result.append(data[index: index + sequence_length])

    if normalise_window:  # 正则化result 。
        result = normalise_windows(result)

    result = np.array(result)

    row = round(0.9 * result.shape[0])  # 精度控制，四舍五入。
    train = result[:int(row), :]  # 生成训练数据 。
    np.random.shuffle(train)
    x_train = train[:, :-1]
    y_train = train[:, -1]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, -1]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return [x_train, y_train, x_test, y_test]








def normalise_windows(window_data):  # 正则化result数据 。
    normalised_data = []
    for window in window_data:
        normalised_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalised_data.append(normalised_window)
    return normalised_data

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


if __name__ == '__main__':
    global_start_time = time.time()
    seq_len = 50
    X_train, y_train, X_test, y_test = load_data('sp501.csv', seq_len, True)

