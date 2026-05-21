from statistics import median

def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    result = []

    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        result.append(median(window))

    return result