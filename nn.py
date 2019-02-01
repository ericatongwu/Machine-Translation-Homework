from LSA import samples
from outs import outs
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
from keras import optimizers
import matplotlib.pyplot as plt

samples = open("sample.txt")
outs = open("outs.txt")
print type(samples)
nadam = optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)
#beta_1 0.9, beta_2 0.999
truth = np.zeros((samples.shape[0], 20))
for l in range(len(outs)):
	truth[l][labels[l]] = 1

X_train, X_test, y_train, y_test = train_test_split(samples, 
													truth, 
													test_size=0.2,  #0.2 original
													random_state=0, 
													shuffle = True)
print y_train
# scores_list = []
# for i in range(100):

model = Sequential()   # creat a neural networking model takes 9 input get 1 output
model.add(Dense(units=80, activation='tanh', input_dim=100))   # create first layer, 50 nodes, activation -> function
model.add(Dense(units=40, activation='tanh'))   # second layer, no need for input_dim
#model.add(Dense(units=25, activation='tanh'))   # third layer, no need for input_dim
model.add(Dense(units=20, activation='softmax'))      # one output, last layer we use linear function which is also the default


model.compile(loss='categorical_crossentropy',    # categorical_crossentropy
              optimizer='nadam',  # adadelta, RMSprop, Adagrad, adam, adamax, nadam
              metrics=['categorical_accuracy'])  			

# train the data
history = model.fit( X_train, y_train, epochs=500, shuffle=False, batch_size = len(y_train),verbose=1)  
# epochs start the epochs as the node size, verbose = 2 -> show more details
scores = model.evaluate(X_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	# scores_list.append(scores[1])


plt.title('Loss VS Epochs')
plt.plot(range(1,501), history.history['loss'], label='Loss')
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Loss')

# print np.mean(scores_list)	
plt.show()