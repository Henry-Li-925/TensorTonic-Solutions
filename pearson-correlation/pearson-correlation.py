import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.shape[0] < 2 or X.ndim != 2: # handle invalid input
        return None
    cov_mat = np.cov(X, rowvar=False, bias=True) # get population covariance
    stds = np.std(X,axis=0)
    denom_mat = np.outer(stds, stds)
    try:
        cor_mat = cov_mat / denom_mat
    except Exception: # handle zero variances
        cor_mat = np.full_like(cov_mat, np.nan)
        np.fill_diagonal(cor_mat, 1)
    return cor_mat 