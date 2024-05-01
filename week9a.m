% Define the differential equation as a function
function dydt = myODE(t, y)
    dydt = -2 * y;
end

% Define the time span
tspan = [0, 5]; % from t = 0 to t = 5

% Define the initial condition
y0 = 1;

% Solve the differential equation
[t, y] = ode45(@myODE, tspan, y0);

% Plot the solution
plot(t, y)
xlabel('Time (t)')
ylabel('y(t)')
title('Solution of the Differential Equation')
grid on
