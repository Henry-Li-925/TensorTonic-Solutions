import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x=np.asarray(x)
    np.place(x, x<0, 0)
    return x