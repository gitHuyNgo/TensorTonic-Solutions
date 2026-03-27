def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    return [float(x) if x > 0 else float(alpha * (math.exp(x) - 1)) for x in x]