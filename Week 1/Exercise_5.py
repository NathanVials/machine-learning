"""
multi-class classification for 4 classes
"""


#import dependencies
import numpy as np
import matplotlib.pyplot as plt

#generate some sample data points
np.random.seed(0)
x = np.random.uniform(0, 8, 300)
y = np.random.uniform(0, 8, 300)

#assign class labels based on the decision boundaries
class_labels = []
for i in range(len(x)):
    if y[i] > 6:
        class_labels.append(4)
    elif x[i] <= 4 and y[i] <= x[i]:
        class_labels.append(1)
    elif x[i] <= 4 and y[i] > x[i]:
        class_labels.append(2)
    else:
        class_labels.append(3)

#create numpy array for class labels
class_labels = np.array(class_labels)

#create scatter plots for each class with different colors
plt.figure(figsize=(8, 6))
plt.scatter(x[class_labels == 1], y[class_labels == 1], c='r', marker='o', label='Class 1')
plt.scatter(x[class_labels == 2], y[class_labels == 2], c='g', marker='s', label='Class 2')
plt.scatter(x[class_labels == 3], y[class_labels == 3], c='b', marker='^', label='Class 3')
plt.scatter(x[class_labels == 4], y[class_labels == 4], c='y', marker='.', label='Class 4')

#plot decision boundaries
plt.plot([0, 4], [0, 4], 'k--', label='Decision Boundary: y=x')
plt.axvline(x=4, color='k', linestyle='--', label='Decision Boundary: x=4')
plt.axhline(y=6, color='k', linestyle='--', label='Decision Boundary: y>6')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Separation of Four Classes based on Decision Boundaries')
plt.grid(True)
plt.show()
