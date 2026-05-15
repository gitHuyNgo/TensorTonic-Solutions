import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.asarray(matrix, dtype=float)
    except:
        return None
        
    if matrix.size == 0:
        return None

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    
    eigenvalues = np.linalg.eigvals(matrix)

    return eigenvalues