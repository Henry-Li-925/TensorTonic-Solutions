import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    mu = np.sum(x) / len(x)
    std = np.sqrt(np.sum(np.pow(np.array(x) - mu, 2))/(len(x) - 1))
    t_stat = (mu - mu0)/(std/np.sqrt(len(x)))
    return t_stat