"""
code generates two classes of data and fits a decision boundary to seperate them
"""


#import dependencies
import numpy as np
import matplotlib.pyplot as plt


#function for the decision boundary line
def decision_boundary(x):
    slope = 1.5
    intercept = 0
    return slope*x + intercept


#class values
x1 = np.random.uniform(low=-2, high=2, size=100)
y1 = np.random.uniform(low=4, high=7, size=100)
x2 = np.random.uniform(low=3, high=7, size=100)
y2 = np.random.uniform(low=0, high=4, size=100)

#plot values
plt.scatter(x1, y1)
plt.scatter(x2, y2)

# Define a range of x-values for plotting
x_values = np.linspace(-3, 8, 100)

# Calculate the corresponding y-values based on the user-provided parameters
y_values = decision_boundary(x_values)

#plot the decision boundary and visualise
plt.plot(x_values, y_values, label='Decision Boundary', color='green')
plt.show()
