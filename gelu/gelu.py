import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.asarray(x)
    def gaussian_cdf(x):
        return 0.5 * (1 + math.erf(x/math.sqrt(2)))
    return x * np.vectorize(gaussian_cdf)(x)