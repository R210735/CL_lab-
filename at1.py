import numpy as np
import matplotlib.pyplot as plt

# Prompting the user to input the lengths of the signals
lx = int(input('Enter the length of signal x(n): '))
ly = int(input('Enter the length of signal y(n): '))

# Generating random signals x(n) and y(n)
x = np.random.rand(lx)
y = np.random.rand(ly)

# Function to compute the summation
def compute_summation(x, y, ln):
    result = []
    for k in range(0, ln, 2):
        summation = np.sum(x[:min(len(x), ln+1-k)] * y[k:min(len(y), k+ln+1)])
        result.append(summation)
    return result

# Compute the summation
ln = min(lx, ly)
result = compute_summation(x, y, ln)

# Plotting
plt.plot(result)
plt.xlabel('Index (k values)')
plt.ylabel('Summation')
plt.title('Summation from n=0 to ln of x(n)y(n+k)')
plt.show()
