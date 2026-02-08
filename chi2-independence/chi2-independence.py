import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    total = np.sum(np.ravel(C))
    row_sum = np.sum(C, axis=1)
    col_sum = np.sum(C, axis=0)
    i, j = np.meshgrid(row_sum, col_sum, indexing='ij')
    mesh_sum = np.column_stack((i.flatten(), j.flatten()))
    exp_freq = (np.prod(mesh_sum, axis=1) / total).reshape((np.array(C).shape))

    chi_sq = (np.pow(C - exp_freq, 2) / exp_freq).flatten().sum()
    return chi_sq, exp_freq