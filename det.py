import numpy as np 
  
# creating a 3X3 Numpy matrix 
n_array = np.array([[55, 25, 15], 
                    [30, 44, 2], 
                    [11, 45, 77]]) 
  
# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 
  
# calculating the determinant of matrix 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 3X3 square matrix:") 
print(int(det)) 
