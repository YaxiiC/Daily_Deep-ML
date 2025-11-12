'''
Reshape Matrix
Write a Python function that reshapes a given matrix into a specified shape. 
if it cant be reshaped return back an empty list [ ]
'''

import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	num_rows= len(a)
	num_cols= len(a[0])
	if num_rows*num_cols != new_shape[0]*new_shape[1]:
		return []
	reshaped_matrix = np.array(a).reshape(new_shape)
	return reshaped_matrix.tolist()
