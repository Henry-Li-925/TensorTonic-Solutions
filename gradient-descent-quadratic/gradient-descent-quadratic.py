def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    def gradient(a,b,x0):
        return 2*a*x0 + b
    for step in range(steps):
        x0 = x0 - lr*gradient(a,b,x0)
    return x0