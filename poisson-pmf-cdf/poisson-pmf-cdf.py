import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf = np.exp(-lam + k * np.log(lam) - np.sum(np.log(np.arange(1, k+1))))
    cdf = np.sum([np.exp(-lam + i * np.log(lam) - np.sum(np.log(np.arange(1, i+1)))) for i in range(k+1)])
    return pmf, cdf