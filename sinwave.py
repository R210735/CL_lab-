import numpy as np
import matplotlib.pyplot as plt
 
# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.cos(x)
 
# Plotting coine Graph
plt.plot(x, y, color='green')
plt.show()
