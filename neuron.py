import numpy as np
import random

class Neuron:
    """
    A class to represent a neuron in a neural network.
    Attributes
    ----------
    index : int
        The index of the neuron.
    weights : np.array
        The weights associated with the neuron's inputs.
    is_refractory : bool
        A flag indicating if the neuron is in a refractory period.
    firing_threshold : float
        The threshold above which the neuron will fire.
    Methods
    -------
    __init__(self, index, weights, firing_threshold=0.5):
        Initializes the neuron with an index, weights, and an optional firing threshold.
    __str__(self):
        Returns a string representation of the neuron.
    weighted_sum(self, inputs):
        Calculates the weighted sum of the inputs.
    sigmoid(self, x):
        Applies the sigmoid activation function to a given input.
    fire(self, weighted_sum):
        Determines if the neuron should fire based on the weighted sum and firing threshold.
    process_inputs(self, inputs):
        Processes the inputs through the neuron and returns the output.
    reset_refractory(self):
        Resets the refractory state of the neuron.
    """

    """
    The __init__ method is a special function in Python. It’s called the initializer or constructor.
    It automatically runs whenever you create a new object of the class.
    It is used to set up the initial state of the object.
    """
    def __init__(self, index, weights, firing_threshold=0.5):
        self.index = index
        self.weights = np.array(weights)
        self.is_refractory = False
        self.firing_threshold = firing_threshold

    """
    __str__ is another special function in Python.
    When you call print(object) or str(object) on a neuron, this method determines what text gets displayed.
    In this case, it will return a string that says something like: "Neuron 1 has 5 inputs".
    """
    def __str__(self):
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
    neur = Neuron(index=1, weights=[0.2, -0.4, 0.5], firing_threshold=0.2)
    print(neur)
    inputs = [0.5, 0.1, -0.3]
    output = neur.process_inputs(inputs)
    print(f"Neuron output: {output}")
    neur.reset_refractory()
    output = neur.process_inputs(inputs)
    print(f"Neuron output: {output}")