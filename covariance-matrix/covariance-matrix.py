import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    N = X.shape[0]
    if N < 2 or X.ndim !=2 :
        return None
    mean_centered = X - np.mean(X, axis=0)
    cov_mat = (mean_centered.T @ mean_centered) / (N-1)
    return cov_mat