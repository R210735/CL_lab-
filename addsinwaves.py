import numpy as np
import matplotlib.pyplot as plt

# Define the x-axis range
x = np.arange(0, 10, 0.1)

# Define the frequencies of the sine waves
freq1 = 1  # Frequency of the first sine wave
freq2 = 2  # Frequency of the second sine wave

# Generate the y-values for the sine waves
y1 = np.sin(2 * np.pi * freq1 * x)  # First sine wave
y2 = np.sin(2 * np.pi * freq2 * x)  # Second sine wave

# Add the two sine waves
y_combined = y1 + y2

# Plotting the individual sine waves
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='Sine Wave 1 ({} Hz)'.format(freq1))
plt.plot(x, y2, label='Sine Wave 2 ({} Hz)'.format(freq2))
plt.title('Two Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the combined sine waves
plt.figure(figsize=(10, 5))
plt.plot(x, y_combined, color='red', label='Combined Sine Waves')
plt.title('Addition of Two Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

