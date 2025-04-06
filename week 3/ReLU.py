#in numPy
def ReLU(x):
    return max(0, x)

#in keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

keras.layers.Dense(25, activation='relu', kernel_initializer=initializer, bias_initializer='zeros')

#Leaky ReLU 
#in numPy
def leaku_ReLu(x):
    return max(0.05*x, x)


#in keras
model = Sequential()
model.add(Dense(90))
model.add(leaku_ReLu(alpha=0.05))
