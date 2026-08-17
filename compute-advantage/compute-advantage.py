import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    rewards = np.asarray(rewards)
    V = np.asarray(V)

    returns = np.zeros(len(rewards))
    G = 0.0

    for t in reversed(range(len(rewards))):
        G = rewards[t] + gamma * G
        returns[t] = G

    A = returns - V

    return A