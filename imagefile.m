pkg load image  % Load the image package if not already loaded

% Read image file
image = imread('input_image.jpg');  % Replace 'input_image.jpg' with the path to your image file

% Convert the image to RGB (assuming it's in RGB format)
if size(image, 3) == 1
    rgb_image = cat(3, image, image, image);  % Convert grayscale to RGB
else
    rgb_image = image;  % Image is already in RGB format
end

% Get RGB values as a 2D matrix
[m, n, ~] = size(rgb_image);
rgb_values = reshape(rgb_image, m*n, 3);

% Write RGB values to CSV file
csvwrite('rgb_values.csv', rgb_values);
