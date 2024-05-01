% Structure of frequencies and amplitudes
parameters.freq1 = 2;
parameters.amp1 = 1.5;
parameters.freq2 = 3;
parameters.amp2 = 2;

% Generate time axis
t = linspace(0, 2*pi, 1000);

% Generate desired sine wave
sinewave = parameters.amp1 * sin(parameters.freq1 * t) + ...
           parameters.amp2 * sin(parameters.freq2 * t);

% Plot the sine wave
plot(t, sinewave)
xlabel('Time')
ylabel('Amplitude')
title('Desired Sine Wave')
grid on
