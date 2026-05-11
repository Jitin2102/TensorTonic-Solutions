import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.array(v)          # ensure it's a NumPy array
    n = len(v)               # length of vector
    diag = np.zeros((n, n))  # start with all zeros
    
    # place v[i] on the diagonal
    for i in range(n):
        diag[i][i] = v[i]
    
    return diag
