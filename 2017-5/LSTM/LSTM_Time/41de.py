#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
from keras.layers import Dense, merge, Activation, Dropout
from keras.models import Model
from keras.models import Sequential
from keras.optimizers import SGD


from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

train = np.random.random((4, 6)) #    #  N行 N列 的随机数。
labels = np.random.randint(10, size=(4, 1)) #   #指定范围的 N行 N列 随机数。
model = Sequential()
model.add(Dense(25, input_shape=(31,),activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.5))
# model.add(Dense(100, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

sgd = SGD(lr=0.01, decay=1e-6)
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(train,labels,nb_epoch=1,batch_size=1)
# model.fit(X_res, y_res,validation_data=(X_test, y_test),nb_epoch=100,batch_size=100)


df = pd.read_csv("training.csv")
y = np.array(df['Label'].apply(lambda x: 0 if x=='s' else 1))
X = np.array(df.drop(["EventId","Label"], axis=1))
sm = SMOTE()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_res, y_res = sm.fit_sample(X_train, y_train)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)


