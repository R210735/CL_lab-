import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation function
def model(y, t):
    dydt = -2 * y  # Example: dy/dt = -2y
    return dydt

# Define the time points
t = np.linspace(0, 5, 100)

# Define the initial condition
y0 = 1

# Solve the differential equation
y = odeint(model, y0, t)

# Plot the solution
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.grid(True)
plt.show()

