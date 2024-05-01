from PIL import Image
import numpy as np

# Read image file
image = Image.open('input_image.jpg')  # Replace 'input_image.jpg' with the path to your image file
rgb_image = image.convert('RGB')

# Get RGB values as a numpy array
rgb_array = np.array(rgb_image)

# Reshape array to a 2D array (rows: pixels, columns: RGB values)
pixels, channels = rgb_array.shape[:-1]
rgb_values = rgb_array.reshape(pixels, channels)

# Write RGB values to CSV file
np.savetxt('rgb_values.csv', rgb_values, delimiter=',')

