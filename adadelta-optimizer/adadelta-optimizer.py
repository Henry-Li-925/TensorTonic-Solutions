import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    # Write code here
    E_grad_sq = np.asarray(E_grad_sq); grad = np.asarray(grad); w = np.asarray(w); E_update_sq = np.asarray(E_update_sq)
    E_grad_sq = rho*E_grad_sq + (1-rho)*np.pow(grad, 2)
    update = - np.sqrt(E_update_sq + eps) / np.sqrt(E_grad_sq + eps) * grad
    E_update_sq = rho * E_update_sq + (1-rho) * np.pow(update, 2)
    w_t = w + update
    return w_t, E_grad_sq, E_update_sq