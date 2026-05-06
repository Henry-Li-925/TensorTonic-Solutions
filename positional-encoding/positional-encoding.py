import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    seq = np.empty((seq_len, d_model))
    rows, cols = np.indices(seq.shape)
    i = cols//2
    odd_mask = cols % 2 != 1
    even_mask = ~odd_mask
    even_seq = np.sin(rows / np.pow(base, 2*i/d_model))
    odd_seq = np.cos(rows / np.pow(base, 2*i/d_model))
    seq = even_seq * odd_mask + odd_seq * even_mask
    return seq