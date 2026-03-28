def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    h, w = len(X), len(X[0])
    m, n = h // pool_size, w // pool_size

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            max_val = float('-inf')
            
            for di in range(pool_size):
                for dj in range(pool_size):
                    val = X[i * pool_size + di][j * pool_size + dj]
                    if val > max_val:
                        max_val = val
            
            result[i][j] = max_val

    return result