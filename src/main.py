from keras.layers import Dense
from keras.models import Sequential, Model
import numpy as np

input_data_file = open("data.txt", "r")
test_data_file = open("data_test.txt", "r")

input_data = np.array([[float(q) for q in c.split()] for c in input_data_file.read().split('\n')])
test_data = np.array([[float(q) for q in c.split()] for c in test_data_file.read().split('\n')])

input_data_file.close()
test_data_file.close()

X = input_data[:, :2]
y = input_data[:, 2]
X_test = test_data[:, :2]
y_test = test_data[:, 2]

print(X.shape)

model = Sequential()
model.add(Dense(12, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=50, batch_size=512)
# evaluate the keras model

_, accuracy = model.evaluate(X, y)

model.summary()

predictions = model.predict(X_test)

print(len(predictions))

test_file = open("test_results", "w")

for p in range(len(predictions)):
    test_file.write(str(int(round(predictions[p][0]))) + ' ' + str(y_test[p]) + '\n')

test_file.close()