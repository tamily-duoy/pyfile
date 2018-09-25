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

def normalise_windows(window_data):  # 正则化result数据 。
    normalised_data = []
    for window in window_data:
        normalised_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalised_data.append(normalised_window)
    return normalised_data





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


if __name__ == '__main__':
    global_start_time = time.time()
    seq_len = 50
    X_train, y_train, X_test, y_test = load_data('F:\\pycharm\\pyfile\\2017-5\\spark00\\数据\\17天气.txt', seq_len, True)