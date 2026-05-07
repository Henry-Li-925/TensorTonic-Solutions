import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    if matrix.ndim != 2: # handle invalid matrix
        return None
    if norm_type not in ['l1', 'l2', 'max']: # handle invalid norm_tyep
        return None
    if axis is not None and axis not in [0, 1]: # handle invalid axis
        return None
    norm_type_dict = {'l1': 1, 'l2': 2, 'max': np.inf}
    norm_vec = np.linalg.vector_norm(matrix, ord=norm_type_dict[norm_type], axis=axis)
    if axis == 0:
        norm_vec = norm_vec[np.newaxis, :]
    elif axis == 1:
        norm_vec = norm_vec[:, np.newaxis]    
    return matrix / np.clip(norm_vec, a_min=1e-4, a_max=np.inf) # zero-division handler
    