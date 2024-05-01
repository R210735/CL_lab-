% Taking two 2D arrays
a = [2, 1; 0, 3];
b = [1, 1; 3, 2];

% Calculating dot product using matrix multiplication
% Note that in Octave, matrix multiplication (*) represents the dot product
% of corresponding rows and columns of the matrices
% We need to transpose one matrix to ensure the dimensions are compatible
% Here, I'm transposing matrix b to get the same output as the Python code
disp(b' * a);