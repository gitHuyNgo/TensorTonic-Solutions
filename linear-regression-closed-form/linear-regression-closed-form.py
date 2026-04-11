import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X, y = np.asarray(X), np.asarray(y)
    
    XtX = X.T @ X

    XtX_inv = np.linalg.inv(XtX)

    w = XtX_inv @ X.T @ y

    return w