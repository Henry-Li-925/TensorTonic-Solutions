import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    # np.dot(x, y)
    if len(x) != len(y):
        raise ValueError
    return np.sum(np.array(x) * np.array(y)).item()