def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    dictionary = set(stopwords)
    result = [token for token in tokens if token not in dictionary]
    return result