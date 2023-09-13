import numpy, random

lr = 1 #learning rate
bias = 1 #value of bias
item1 = 0.2
item2 = 0.4
item3 = 0.5
sack = 1
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)

def Perceptron(item1, item2, empty) :
   output = item1*weights[0] + item2*weights[1] + bias*weights[2]
   output = 1/(1+numpy.exp(-output)) #sigmoid function
   error = empty - output
   weights[0] += error * item1 * lr
   weights[1] += error * item2 * lr
   weights[2] += error * bias * lr
   
for i in range(5000) :
   Perceptron(item1, item2, sack - item1 - item2)
   Perceptron(item1, item3, sack - item1 - item3)
   Perceptron(item2, item3, sack - item2 - item3)

x = float(input())
y = float(input())
z = float(input())
output1 = x*weights[0] + y*weights[1] + bias*weights[2]
output2 = x*weights[0] + z*weights[1] + bias*weights[2]
output3 = y*weights[0] + z*weights[1] + bias*weights[2]

all = [output1, output2, output3]
small = min(all)

print(all)
print(small)
