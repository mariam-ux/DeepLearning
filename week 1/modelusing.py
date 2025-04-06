import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

model = Sequential()

model.add(Dense(units=64, activation='relu', name="layer1"))
model.add(Dense(units=10, activation='softmax', name="layer2"))
model.add(Dense(4, name="layer3"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(optimizer= tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True), loss=tf.keras.losses.categorical_crossentropy)

model.summary()

x_train = x_train.reshape(-1, 1)
model.fit(x_train, y_train, epochs=5, batch_size=32)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

calsses = model.predict(x_test, batch_size=128)