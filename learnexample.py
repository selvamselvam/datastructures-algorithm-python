import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np

x_input = np.array([[1, 2, 3, 4, 5]])
y_input = np.array([[10]])

model = Sequential()
model.add(Dense(units=32, activation="tanh", input_dim=x_input.shape[1], kernel_initializer='random_normal'))
model.add(Dense(units=1, kernel_initializer='random_normal'))

model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])

model.summary()

history = model.fit(x_input, y_input, epochs=10, batch_size=32)
model.predict(x_input, batch_size=128)
model.predict(np.array([[1, 2, 5, 4, 5]]))
