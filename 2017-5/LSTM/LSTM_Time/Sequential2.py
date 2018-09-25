#!/usr/bin/python
# -*- coding:utf-8 -*-
#序贯模型是多个网络层的线性堆叠，也就是“一条路走到黑”。
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import keras
from LSTM.LSTM_Time.mode import f1de

model = Sequential()
model.add(Dense(23, activation='relu', input_dim=6))

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

data = np.random.random((4, 6)) #    #  N行 N列 的随机数。
labels = np.random.randint(10, size=(4, 1)) #   #指定范围的 N行 N列 随机数。
# data,labels=f1de.loaddata('17天气d.txt',2)
print("=====测试=====")
print(data)
print("=====")
print(labels)
# data=f1de.loaddata('17天气d.txt',2)


one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

model.fit(data, one_hot_labels, epochs=10, batch_size=32)