% Creating data for plotting
x = 0:0.1:10;
y1 = sin(x);
y2 = cos(x);

% Creating a figure with two subplots arranged vertically
subplot(2, 1, 1);  % 2 rows, 1 column, subplot 1
plot(x, y1);
title('Sine Wave');
xlabel('x');
ylabel('sin(x)');

subplot(2, 1, 2);  % 2 rows, 1 column, subplot 2
plot(x, y2);
title('Cosine Wave');
xlabel('x');
ylabel('cos(x)');
