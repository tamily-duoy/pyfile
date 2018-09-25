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
from LSTM.LSTM_Time import lstm


def load_data(filename, seq_len, normalise_window):    ###
	x_train = []; y_train = [] ; x_test = [] ; y_test = []
	return [x_train, y_train, x_test, y_test]
def normalise_windows(window_data):   ###  load_data
	normalised_data = []
	return normalised_data
def build_model(layers):        ###
	model = Sequential()
	return model
def predict_point_by_point(model, data):
	predicted = model.predict(data)
	return predicted
def predict_sequence_full(model, data, window_size):
	predicted = []
	return predicted
def predict_sequences_multiple(model, data, window_size, prediction_len): ###
	prediction_seqs = []
	return prediction_seqs

def plot_results(predicted_data, true_data):
    plt.show()
def plot_results_multiple(predicted_data, true_data, prediction_len):  ###
    plt.show()
if __name__=='__main__':
	global_start_time = time.time(); epochs  = 1; seq_len = 50
	X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', seq_len, True)
	model = lstm.build_model([1, 50, 100, 1])
	model.fit(X_train,y_train,batch_size=512,nb_epoch=epochs,validation_split=0.05)
	predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, 50)
	print('Training duration (s) : ', time.time() - global_start_time)
	plot_results_multiple(predictions, y_test, 50)