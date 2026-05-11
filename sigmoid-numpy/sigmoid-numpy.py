import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    arr = np.array(x)
    sigma  = 1 / ( 1  + np.exp(-arr))
    return sigma