from neuron import Neuron
import random

weights = [random.uniform(-1, 1) for _ in range(5)] 
neuron = Neuron(1,weights)
inputs = [0.4, 0.3, 0.2, 0.1, 0.5]
output = neuron.process_inputs(inputs)
print("Neuron fired:", output)
    