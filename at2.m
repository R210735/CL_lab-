% Generate random signal
X = rand(1, 1000);

% Function to compute energy for every twenty amplitudes
function energies = compute_energy(signal)
    energies = [];
    for i = 1:20:length(signal)
        energy = sum(signal(i:min(i+19, end)).^2);
        energies = [energies, energy];
    end
end

% Compute energy
energies = compute_energy(X);

% Plotting
plot(energies);
xlabel('Index (every 20 amplitudes)');
ylabel('Energy');
title('Energy for every twenty amplitudes');