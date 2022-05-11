# == DNN algorithm == 

import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('resource_data_total.csv')
data = data.to_numpy()
np.random.shuffle(data)

train_data = data[:,:-1] #train
results = data[:,-1] #test

x_train = train_data[:15000]
y_train = results[:15000]
x_test = train_data[15000:]
y_test = results[15000:]

y_train = y_train.reshape(15000,1)
y_test = y_test.reshape(5000, 1)

scaler = MinMaxScaler()
scaler.fit(x_train)

s_train = scaler.transform(x_train)
s_test = scaler.transform(x_test)
# print(s_train.shape, y_train.shape, s_test.shape, y_test.shape)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=64, activation='relu', input_shape=(14,)))
model.add(tf.keras.layers.Dense(units=32, activation='relu'))
model.add(tf.keras.layers.Dense(units=14, activation='relu'))
# model.summary()

model.compile(tf.keras.optimizers.SGD(), loss='mse', metrics = ['accuracy'])
history = model.fit(x_train, y_train, batch_size=10, epochs=10)

# == ENSENBLE algorithm ==
# from sklearn import ensemble
# import joblib
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split

# data = pd.read_csv('resource_data_total.csv')
# data = data.to_numpy()
# np.random.shuffle(data)

# train_data = data[:,:-1] #train
# results = data[:,-1] #test

# x_train = train_data[:15000]
# y_train = results[:15000]
# x_test = train_data[15000:]
# y_test = results[15000:]

# model = ensemble.RandomForestClassifier(n_estimators=20, max_leaf_nodes=16, n_jobs=-1)
# model.fit(x_train, y_train)

# predictions = model.predict(x_test)
# print(f"Model accuracy: {accuracy_score(y_test, predictions) * 100}")