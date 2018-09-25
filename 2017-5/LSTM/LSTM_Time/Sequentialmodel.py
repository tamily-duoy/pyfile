#!/usr/bin/python
# -*- coding:utf-8 -*-
#序贯模型是多个网络层的线性堆叠，也就是“一条路走到黑”。
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import keras
# #1/  可以通过向Sequential模型传递一个layer的list来构造序贯模型：
# model = Sequential([
#                     Dense(32, units=784),
#                     Activation('relu'),
#                     Dense(10),
#                     Activation('softmax'),
#                     ])
## 2/  也可以通过.add()方法一个个的将layer加入模型中：
# model = Sequential()
# model.add(Dense(32, input_shape=(784,)))
# model.add(Activation('relu'))

#指定输入数据的shape:
#第一层:接受关于输入数据的shape参数，
#后面各层：自动的推导出中间数据的shape，

model = Sequential()
model.add(Dense(23, activation='relu', input_dim=10)) #   #2D层，指定其输入维度input_dim来隐含的指定输入数据shape
     #输出层数，可任意                                                    #一些3D的时域层支持通过参数input_dim和input_length来指定输入shape。
# model = Sequential()
# model.add(Dense(32, input_shape=784))  #input_shape是一个tuple类型的数据，None=表示取正整数


model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Generate dummy data

data = np.random.random((100, 10)) #    #  N行 N列 的随机数。

labels = np.random.randint(10, size=(100, 1)) #   #指定范围的 N行 N列 随机数。

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10) #class vector (integers)转换为 binary class matrix.
#class vector 转换为a matrix (integers from 0 to num_classes).
# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)