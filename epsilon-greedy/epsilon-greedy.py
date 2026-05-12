import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    # Write code here
    q_values = np.asarray(q_values)

    if rng is None:
        rng = np.random.default_rng()

    if rng.random() < epsilon:
        return rng.integers(len(q_values))

    return np.argmax(q_values)