'''
Calculate Mean by Row or Column
Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. 
The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
'''

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if mode == 'column':

        mean=[]
        for j in range(num_cols):
            column_sum = sum(matrix[i][j] for i in range(num_rows))
            column_mean = column_sum / num_rows
            mean.append(column_mean)
        return mean
    
    if mode == 'row':
        mean=[]
        for i in range(num_rows):
            row_sum = sum(matrix[i][j] for j in range(num_cols))
            row_mean = row_sum / num_cols
            mean.append(row_mean)
        return mean

	return mean