import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    id_mat = np.identity(np.array(A).shape[0])
    # square check 
    if np.array(A).shape[0] != np.array(A).shape[1]:
        return None
    # singularity check
    try:
        np.linalg.solve(A, id_mat)
    except:
        return None
    # avoid explicit inversion, instead, solve Ax = I
    return np.linalg.solve(A, id_mat)