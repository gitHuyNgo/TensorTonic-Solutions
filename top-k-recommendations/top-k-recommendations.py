def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    rated_set = set(rated_indices)

    result = [(scores[i], i) for i in range(len(scores)) if i not in rated_set]

    result.sort(key=lambda x: -x[0])

    return [i for _, i in result[:k]]