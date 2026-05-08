import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    # handle non-square matrix
    try:
        matrix = np.asarray(matrix)        
    except:
        return None
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    eigs = np.linalg.eigvals(matrix)
    eigs = np.sort(eigs)
    return eigs