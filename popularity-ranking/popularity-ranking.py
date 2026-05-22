def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    ranked_items = []

    for item in items:
        R = item[0]
        v = item[1]
        m = min_votes
        C = global_mean
        score = (v / (v + m)) * R + (m / (v + m)) * C
        ranked_items.append(score)

    return ranked_items