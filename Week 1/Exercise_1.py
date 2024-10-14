"""
Piece of code that creates and displays two different classes of arbitrarily generated data
np.random.uniform function creates a uniform distribution of values between a specified high and low point
these distributed datasets are visualised in a scatter plot
"""




#import dependencies
import numpy as np
import matplotlib.pyplot as plt


#generate values
x1 = np.random.uniform(low=-2, high=2, size=100)
y1 = np.random.uniform(low=4, high=7, size=100)
x2 = np.random.uniform(low=3, high=7, size=100)
y2 = np.random.uniform(low=0, high=4, size=100)

#plot values
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.show()