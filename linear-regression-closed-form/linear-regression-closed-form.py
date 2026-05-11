import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    x_arr = np.array(X)
    y_arr = np.array(y)
    x_T = x_arr.T
    p1 = np.dot(x_T,x_arr)
    inv = np.linalg.inv(p1)
    p2 = np.dot(x_T,y)
    res = np.dot(p2,inv)
    return res