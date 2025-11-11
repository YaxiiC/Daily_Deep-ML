
'''
Transpose_of_a_Matrix
Write a Python function that computes the transpose of a given matrix.
'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	
    num_rows= len(a)
    num_cols= len(a[0])
    #initialize the transpose matrix with zeros
    b = []
    for _ in range(num_cols):
        row = []
        for _ in range(num_rows):
            row.append(0)
        b.append(row)
    
    for i in range(num_rows):
        for j in range (num_cols):
            b[j][i]= a[i][j]

    return b

print(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))