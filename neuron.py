import numpy as np
import random

class Neuron:
    def __init__(self, index, weights, firing_threshold=0.5):
        self.index = index
        self.weights = np.array(weights)
        self.is_refractory = False
        self.firing_threshold = firing_threshold

    def __string__(self):
        return f"Neuron {self.index} has {len(self.weights)} inputs"

    def weighted_sum(self, inputs):
        return sum(w * i for w, i in zip(self.weights, inputs))
        # equivalent to np.dot(self.weights, inputs)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fire(self, weighted_sum):
        # Apply the sigmoid function to the weighted sum
        activation = self.sigmoid(weighted_sum)
        # Check if neuron should fire based on the activation result
        if activation > self.firing_threshold and not self.is_refractory:
            self.is_refractory = True
            return 1  # Neuron fires
        return 0  # Neuron does not fire

    def process_inputs(self, inputs):
        weighted_sum = self.weighted_sum(inputs)
        output = self.fire(weighted_sum)
        return output

    def reset_refractory(self):
        self.is_refractory = False

# When you run a Python script, Python sets __name__ to the string "__main__" if the script is executed as the main program.
# If the script is imported as a module in another script, __name__ is set to the name of the script/module.
if __name__ == "__main__":
    neuron = Neuron(index=1, weights=[0.2, -0.4, 0.5], firing_threshold=0.2)
    inputs = [0.5, 0.1, -0.3]
    output = neuron.process_inputs(inputs)
    print(f"Neuron output: {output}")
    output = neuron.process_inputs(inputs)
    print(f"Neuron output: {output}")