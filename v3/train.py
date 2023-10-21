from settings import *
from keras.models import Sequential
from keras.layers import Dense


file = open(S.datafile, 'r')
data_rows = file.readlines()

for i in range(100): # the data starts earlier...
    if S.data_start_str in data_rows[i]:
        data_rows = data_rows[ i + 1 : ]


train_input = []
train_output = []

test_input = []
test_output = []

train_count = int( len(data_rows) * S.train_ratio ) - 1
test_count = len(data_rows) - train_count - 1


for i in range(train_count):
    data = data_rows[i].split(',')

    for i in range(len(data)):
        data[i] = float(data[i])
    
    vol_count = S.volume_category_count
    wgt_count = S.weight_category_count

    train_input.append( data[ : vol_count + wgt_count ] )
    train_output.append( data[ vol_count + wgt_count : ] )

for i in range(train_count, len(data_rows)):
    data = data_rows[i].split(',')

    for i in range(len(data)):
        data[i] = float(data[i])
    
    vol_count = S.volume_category_count
    wgt_count = S.weight_category_count

    test_input.append( data[ : vol_count + wgt_count ] )
    test_output.append( data[ vol_count + wgt_count : ] )



model = Sequential()

input_count = S.volume_category_count + S.weight_category_count
output_count = S.volume_category_count

# Input layer
model.add(Dense(input_count, input_dim=input_count, activation='sigmoid'))

# Hidden layers
for _ in range(S.hidden_layer_count):
    model.add(Dense(input_count, activation='sigmoid'))

# Output layer
model.add(Dense(output_count, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.summary()


# Train the model
history = model.fit(
    train_input, 
    train_output, 
    epochs=S.epoch_count, 
    validation_data=(test_input, test_output), 
    verbose=2)


# Evaluate the model on the test set
loss = model.evaluate(test_input, test_output)

print("Final Loss:", loss)


# Save the trained model
model_json = model.to_json()

with open(S.modelfile, 'w') as json_file:
    json_file.write(model_json)

model.save_weights(S.weightsfile)
