import numpy as np

'''
Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. 
For example, an n x m matrix requires a vector of length m.
'''
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a or not a[0]: # check if the matrix is empty
        return -1

    num_rows = len(a)
    num_cols = len(a[0])
    
    if len(b) != num_cols:
        return -1 # check if the vector is compatible with the matrix
    
    results = []
    for row in a:
        if len(row) != num_cols: # check if the row is compatible with the matrix
            return -1 # check if the row is compatible with the matrix
        dot = sum(row[i]*b[i] for i in range(num_cols))
        results.append(dot) # append the dot product to the results list
        
    return results

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if not a or not a[0]:
        return -1
    
    num_rows = len(a)
    num_cols = len(a[0])
    
    if len(b) != num_cols:
        return -1
    
    results = []
    for row in a:     
        
        c = sum(row[j]*b[j] for j in range(num_cols))
        results.append(c) # append the dot product to the results list
    
    return results