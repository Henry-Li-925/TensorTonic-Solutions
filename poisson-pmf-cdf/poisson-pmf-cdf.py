import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    def log_pmf(lam, k):
        if k != 0:
            k_seq = np.arange(1,k+1)
        else:
            k_seq = [1]        
        def log_num(lam, k):
            return -lam + k * np.log(lam)
        def log_factorial(fac_seq):
            return np.sum(np.log(fac_seq))
        return log_num(lam,k) - log_factorial(k_seq)
    pmf = np.exp(log_pmf(lam, k))

    ind = np.arange(k+1)
    cdf = np.sum([np.exp(log_pmf(lam, i)) for i in ind])
    return pmf, cdf