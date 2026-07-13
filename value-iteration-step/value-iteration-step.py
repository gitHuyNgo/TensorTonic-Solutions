import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    values = np.asarray(values)
    transitions = np.asarray(transitions)
    rewards = np.asarray(rewards)
    
    q = rewards + gamma * np.einsum('sak,k->sa', transitions, values)
    return q.max(axis=1).tolist()