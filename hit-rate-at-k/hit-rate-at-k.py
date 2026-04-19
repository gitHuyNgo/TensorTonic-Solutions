def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hits = 0
    n = len(recommendations)

    for recs, gt in zip(recommendations, ground_truth):
        top_k = recs[:k]
        if any(item in gt for item in top_k):
            hits += 1

    return hits / n