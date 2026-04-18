def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    N = len(actual_tokens)
    
    log_prob_sum = 0.0

    for i in range(N):
        prob = prob_distributions[i][actual_tokens[i]]

        if prob <= 0:
            return float('inf')

        log_prob_sum += math.log(prob)

    return math.exp(-log_prob_sum / N)