from keras.models import Sequential  # neural network will work sequentially
from keras.layers.core import Dense  # Fully Connected
import numpy as np

# Supervised Learning

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# print(x)

model = Sequential()
model.add(Dense(4, input_dim=2, activation="sigmoid"))
model.add(Dense(1, input_dim=4, activation="sigmoid"))

# print(model.weights)

model.compile(
    loss="mean_squared_error", optimizer="adam", metrics=["binary_accuracy"]
)  # binary_accuracy is going to measure the accuracy of the given model i.e NN

# print(model.weights)

model.fit(x, y, epochs=10000, verbose=2)

print(model.predict(x))
