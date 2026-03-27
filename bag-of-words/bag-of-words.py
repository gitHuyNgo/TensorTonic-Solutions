import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    token_counts = Counter(tokens)

    vector = [token_counts[word] for word in vocab]

    return np.array(vector, dtype=int)