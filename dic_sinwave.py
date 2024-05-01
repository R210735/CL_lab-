import numpy as np
import matplotlib.pyplot as plt

# Dictionary of frequencies and amplitudes
parameters = {'freq1': 2, 'amp1': 1.5, 'freq2': 3, 'amp2': 2}

# Generate time axis
t = np.linspace(0, 2*np.pi, 1000)

# Generate desired sine wave
sinewave = parameters['amp1'] * np.sin(parameters['freq1'] * t) + \
           parameters['amp2'] * np.sin(parameters['freq2'] * t)

# Plot the sine wave
plt.plot(t, sinewave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Desired Sine Wave')
plt.grid(True)
plt.show()

