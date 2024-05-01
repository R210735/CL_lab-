% Creating x axis with range and y axis with Sine Function for Plotting Sine Graph
x = 0:0.1:5;
%y = sin(x);
y = builtin('sin', x);
% Plotting Sine Graph
plot(x, y, 'g');
xlabel('x');
ylabel('sin(x)');
title('Sine Graph');
grid on;
