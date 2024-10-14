"""
code generates two classes of data, fits a decision boundary,
and then classifies newly introduced samples
"""


#import dependencies
import numpy as np
import matplotlib.pyplot as plt


#function for the decision boundary line
def decision_boundary(x):
    slope = 1.1
    intercept = 1
    return slope*x + intercept


#sample values
x_coords = [-4, -2, 0, -6, -4, -2]
y_coords = [-4, -4, 0, 0, 2, 2]

#class values
x1 = np.random.uniform(low=-2, high=2, size=100)
y1 = np.random.uniform(low=4, high=7, size=100)
x2 = np.random.uniform(low=3, high=7, size=100)
y2 = np.random.uniform(low=0, high=4, size=100)

#new class values
class1_x = [-6, -4, -2]
class1_y = [0, 2, 2]
class2_x = [-4, -2, 0]
class2_y = [-4, -4, 0]

#plot values
plt.scatter(x1, y1, color='b')
plt.scatter(x2, y2, color='orange')
plt.scatter(class1_x, class1_y, color='b')
plt.scatter(class2_x, class2_y, color='orange')

# Define a range of x-values for plotting
x_values = np.linspace(-8, 8, 100)

# Calculate the corresponding y-values
y_values = decision_boundary(x_values)

#plot the decision boundary
plt.plot(x_values, y_values, label='Decision Boundary', color='green')
plt.show()
