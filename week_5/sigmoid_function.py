import numpy
import matplotlib.pyplot

# Define the activation function
def activation(weighted_sum):
    return 1 / (1 + numpy.exp(-weighted_sum))

# Generate a range of values from -10 to 10 to represent weighted sums
weighted_sums = numpy.linspace(-10, 10, 200)

# Calculate the activation values for each weighted sum
activation_values = activation(weighted_sums)

# Plot the activation function
matplotlib.pyplot.figure(figsize=(10, 6))
matplotlib.pyplot.plot(weighted_sums, activation_values, label="Sigmoid Activation")
matplotlib.pyplot.title("Sigmoid Activation Function")
matplotlib.pyplot.xlabel("Weighted Sum")
matplotlib.pyplot.ylabel("Activation")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()