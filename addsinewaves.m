clc
clear all
close all

% Define time vector with smaller step size to ensure matching dimensions
t = 0:0.01:1;

f1 = 4;
f2 = 2;

x = sin(2*pi*f1*t);
y = sin(2*pi*f2*t);

z = x + y;

plot(t, x);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave with Frequency f1 = 4 Hz');
grid on;
