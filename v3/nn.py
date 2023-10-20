from settings import *
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

file = open('./data/2023-10-20 09:09:32.450666c', 'r')
data_rows = file.readlines()

for i in range(100):
    if 'DATA START' in data_rows[i]:
        data_rows = data_rows[ i + 1 : ]


train_input = []
train_output = []

test_input = []
test_output = []

train_count = int( len(data_rows) * 0.9 ) - 1
test_count = len(data_rows) - train_count - 1


for i in range(train_count):
    data = data_rows[i].split(',')

    for i in range(len(data)):
        data[i] = float(data[i])
    
    vc = S.volume_category_count
    wc = S.weight_category_count

    train_input.append( data[ : vc + wc ] )
    train_output.append( data[ vc + wc : ] )

for i in range(train_count, len(data_rows)):
    data = data_rows[i].split(',')

    for i in range(len(data)):
        data[i] = float(data[i])
    
    vc = S.volume_category_count
    wc = S.weight_category_count

    test_input.append( data[ : vc + wc ] )
    test_output.append( data[ vc + wc : ] )




# Define the neural network model
model = Sequential()

# Input layer with 12 units
model.add(Dense(12, input_dim=12, activation='sigmoid'))

# Six hidden layers with sigmoid activation
for _ in range(6):
    model.add(Dense(12, activation='sigmoid'))

# Output layer with 6 units
model.add(Dense(6, activation='sigmoid'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Print the model summary
model.summary()



# Assuming you have X_train and y_train for training data
# X_test and y_test for testing data

# Compile the model (if not done already)
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
history = model.fit(train_input, train_output, epochs=50, validation_data=(test_input, test_output))

# Evaluate the model on the test set
loss = model.evaluate(test_input, test_output)

# Print the final loss
print("Final Loss:", loss)



