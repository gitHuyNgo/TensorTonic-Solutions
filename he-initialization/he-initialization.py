def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = np.array(math.sqrt(6 / fan_in))
    W = np.array(W)

    return W * 2 * L - L