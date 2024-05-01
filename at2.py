import numpy as np
import matplotlib.pyplot as plt

# Generate random signal
X = np.random.rand(1000)

# Function to compute energy for every twenty amplitudes
def compute_energy(signal):
    energies = []
    for i in range(0, len(signal), 20):
        energy = np.sum(signal[i:min(i+20, len(signal))]**2)
        energies.append(energy)
    return energies

# Compute energy
energies = compute_energy(X)

# Plotting
plt.plot(energies)
plt.xlabel('Index (every 20 amplitudes)')
plt.ylabel('Energy')
plt.title('Energy for every twenty amplitudes')
plt.show()

