import copy
import numpy as np
from keras.models import model_from_json
from v5.settings import *
from v5.settings import *
from v5.reserve import *
from v5.sack import *


def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()
        if not sack.add(item): return sack



# Load the model architecture from the JSON file
with open(S.modelfile, 'r') as json_file:
    loaded_model_json = json_file.read()
    
model = model_from_json(loaded_model_json)

# Load the model weights from the HDF5 file
model.load_weights(S.weightsfile)

# Compile the loaded model if you intend to continue training or using it
model.compile(loss='mean_squared_error', optimizer='adam')


for _ in range(S.total_iterations):
    sack_distrs = []
    sack_values = []
    reserve = Reserve()

    for __ in range(S.iterations):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        if filled_sack.getTotalVolume() > res_copy.getTotalVolume():
            print('All reserve items fits in the sack, discarded...')
            continue

        sack_distrs.append(filled_sack.getVolumeDistribution())
        sack_values.append(filled_sack.getTotalValue())

    if not sack_distrs: continue

    best_sack_index = sack_values.index(max(sack_values))
    best_sack_distr = sack_distrs[best_sack_index]

    worst_sack_index = sack_values.index(min(sack_values))
    worst_sack_distr = sack_distrs[worst_sack_index]

    input_data = reserve.getVolumeDistribution() + reserve.getWeightDistribution()
    # Assuming your input data is in a variable 'input_data'
    # Reshape the input data to have two dimensions
    input_data = np.reshape(input_data, (1, -1))
    print(f'prediction:\t{model.predict( input_data )}')









