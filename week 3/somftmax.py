#in numpy
import numpy as np

def softmax(x, neuron):
    e_x = np.exp(x-np.max(x))
    return (e_x/e_x.sum(axis=0))

#in keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(90))
model.add(Dense(units=10, activation='softmax'))