% Creating a 3x3 matrix
n_array = [55, 25, 15;
           30, 44, 2;
           11, 45, 77];

% Displaying the matrix
disp("Numpy Matrix is:");
disp(n_array);

% Calculating the determinant of the matrix
det = det(n_array);

disp("\nDeterminant of given 3x3 square matrix:");
disp(det);
