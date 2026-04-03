def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    X, W, b = np.asarray(X), np.asarray(W), np.asarray(b)
    
    Y = X @ W + b

    return Y.tolist()