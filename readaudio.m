pkg load audio  % Load the audio package

% Load audio file
[y, Fs] = audioread('/home/rgukt/Downloads/Chorus.wav');

% Create time vector
t = (0:length(y)-1) / Fs;

% Plot audio signal
plot(t, y)
xlabel('Time (s)')
ylabel('Amplitude')
title('Audio Signal')
