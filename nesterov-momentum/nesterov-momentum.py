import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here
    v_t = momentum * np.asarray(v) + lr * np.asarray(grad)
    w_t = w - v_t 
    return w_t, v_t