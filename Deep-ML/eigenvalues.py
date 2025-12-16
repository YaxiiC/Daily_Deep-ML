'''
The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is 

λ are the eigenvalues.
'''

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]

    # Trace and determinant
    trace = a + d
    det = a*d - b*c

    # Discriminant
    discriminant = trace**2 - 4*det

    # Eigenvalues
    lambda1 = (trace + discriminant**0.5) / 2
    lambda2 = (trace - discriminant**0.5) / 2

    # Return sorted from highest to lowest
    return sorted([lambda1, lambda2], reverse=True)