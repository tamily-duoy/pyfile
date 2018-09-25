#!/usr/bin/python
# -*- coding:utf-8 -*-
#序贯模型是多个网络层的线性堆叠
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import keras
from LSTM.LSTM_Time.mode import f1de


model = Sequential()
model.add(Dense(23, activation='relu', input_dim=2))

model.add(Dense(30, activation='softmax'))  #num_classes

model.compile(optimizer='rmsprop',
              loss='mse',
              metrics=['accuracy'])

# data = np.random.random((2, 2)) #    #  N行 N列 的随机数。
# labels = np.random.randint(2, size=(2, 1)) #   #指定范围的 N行 N列 随机数。
data,labels=f1de.loaddata('17天气de.txt',2)
# data,labels,xtest,ytest=f1de.loaddata('17天气de.txt',2)
print("=====测试=====")
# print(data)
# print("=====")
# print(labels)

one_hot_labels = keras.utils.to_categorical(labels, num_classes=30)
# print(one_hot_labels)
model.fit(data, one_hot_labels, epochs=5, batch_size=6)
classes = model.predict_classes(data)
