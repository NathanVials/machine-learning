"""
code generates a regression line, with different functions for differnet x values
"""


#import dependencies
import numpy as np
import matplotlib.pyplot as plt

# Define the range of the x values
x=np.linspace(0,20,400)

# Initialize an empty array for y values
y=np.empty_like(x)

# Calculate y values based on the piecewise function
for i, xi in enumerate(x):
    if xi<= 2:
        y[i]= pow(xi,3)
    elif xi> 2 and xi <=10:
        y[i] = 2*xi+4
    else:
        y[i] = 0.5*xi * xi -22

# Plot the function
plt.figure(figsize=(8,6))
plt.plot(x,y,label='Regression Line')
plt.xlim(0,20)
plt.ylim(0,84)
plt.xticks(np.arange(0, 20, 1), fontsize=12)
plt.yticks(np.arange(0, 84, 4), fontsize=12)
plt.xlabel('x-value', fontsize=22)
plt.ylabel('y-value',fontsize =22)
plt.legend(fontsize=24)
plt.grid(True)
plt.show()
