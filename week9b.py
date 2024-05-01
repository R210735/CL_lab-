import numpy as np
import matplotlib.pyplot as plt

# Creating data for plotting
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating a figure with two subplots arranged vertically
plt.subplot(2, 1, 1)  # 2 rows, 1 column, subplot 1
plt.plot(x, y1)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.subplot(2, 1, 2)  # 2 rows, 1 column, subplot 2
plt.plot(x, y2)
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('cos(x)')

plt.tight_layout()  # Adjust subplots to fit into the figure area
plt.show()

