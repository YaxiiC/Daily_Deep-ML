'''
Write a Python function that multiplies a matrix by a scalar and returns the result.
'''
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	num_cols= len(matrix[0])
    num_rows= len(matrix)


    result=[]
    for row in matrix:
    
        new_row = []
        for i in range (num_cols):
            row[i]=row[i]*scalar
            new_row.append(row[i])
        
        result.append(new_row)
        
    
    return result