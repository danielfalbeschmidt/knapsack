from settings import *
import math, random

class nn:
    weights = [] # [input, hidden, output]
    input_count = S.volume_category_count + S.weight_category_count

    def initWeights():
        w0 = [] # input layer weights

        for _ in range(nn.input_count):
            w0.append(random.random())

        nn.weights.append(w0)

        for tier in range(S.hidden_layer_count):
            wh = [] # hidden layers, last is output

            n = nn.input_count - nn.getNeuronCount(tier)
            for _ in range(n):
                wh.append(random.random())

            nn.weights.append(wh)
        
    def getNeuronCount(tier): # 1 - S.hidden_layer_count
        tier += 1
        count_diff = nn.input_count - S.volume_category_count
        count_coef = count_diff / S.hidden_layer_count
        return int( count_coef * tier )

    def learn(input, exp_output, success_rate):
        act_output = nn.feed(input, index=0)
        nn.backP(exp_output, act_output, success_rate, index=( len(nn.weights) - 1 ))

    def feed(input, index):
        if index >= len(nn.weights) - 1: return input

        in_weights = nn.weights[index]
        output = []

        for _ in range(len(nn.weights[index + 1])):
            w_sum = 0

            for i in range(len(in_weights)):
                w_sum += input[i] * in_weights[i]

            output.append( nn.sigmoid( w_sum + S.bias ) )

        index += 1
        nn.feed(output, index)

    def backP(expected, actual, success_rate, index):
        if index < 1: return

        output = []

        for i in range(len(nn.weights[index])):
            cost = ( ( expected[i] / actual[i] ) - 1 )
            cost *= ( S.learning_rate / success_rate )

            w_sum = 0

            for i in range(len(actual)):
                nn.weights[index][i] = 

            output.append(w_sum)

        index -= 1
        nn.backP(output, success_rate, index)

    def sigmoid(x):
        return 1 / ( 1 + math.exp( -x ) )
    
    def printOutputWeights():
        print(nn.weights[len(nn.weights) - 1])