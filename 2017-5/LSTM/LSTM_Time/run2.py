# LSTM-Neural-Network-for-Time-Series-Prediction-master
from LSTM.LSTM_Time import lstm
import time
import matplotlib.pyplot as plt


def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    #Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
        plt.legend()
    plt.show()

#Main Run Thread
if __name__=='__main__':
	global_start_time = time.time()
	epochs  = 1   # one forward pass and one backward pass of all the training examples
	seq_len = 50

	print('> Loading data... ')

	X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', seq_len, True)
	print(X_train)

	print('> Data Loaded. Compiling...')

	model = lstm.build_model([1, 50, 100, 1])

	model.fit(
	    X_train,
	    y_train,
	    batch_size=512,
	    nb_epoch=epochs,
	    validation_split=0.05)

	predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, 50)
	print('Training duration (s) : ', time.time() - global_start_time)
	plot_results_multiple(predictions, y_test, 50)