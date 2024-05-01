import numpy as np
import matplotlib.pyplot as plt

# Define the time axis
t = np.linspace(0, 1, 1000)

# Define the waves
wave1 = np.sin(2 * np.pi * 5 * t)  # Wave with frequency 5 Hz
wave2 = np.sin(2 * np.pi * 3 * t)  # Wave with frequency 3 Hz

# Subtract the waves
result_wave = wave1 - wave2

# Plot the original waves and the result
plt.figure(figsize=(10, 5))
plt.plot(t, wave1, label='Wave 1 (5 Hz)')
plt.plot(t, wave2, label='Wave 2 (3 Hz)')
plt.plot(t, result_wave, label='Subtraction Result')
plt.title('Subtraction of Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

