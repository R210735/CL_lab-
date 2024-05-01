X = [1, 2, 3;
     4, 5, 6;
     7, 8, 9];
 
Y = [9, 8, 7;
     6, 5, 4;
     3, 2, 1];
 
result = zeros(size(X)); % Initialize result matrix with zeros of the same size as X
 
% iterate through rows
for i = 1:size(X, 1)
    % iterate through columns
    for j = 1:size(X, 2)
        result(i, j) = X(i, j) + Y(i, j);
    end
end
 
disp(result);