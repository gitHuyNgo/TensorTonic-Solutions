def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    m, n = len(s1), len(s2)
    result = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        result[i][n] = m - i
    for j in range(n + 1):
        result[m][j] = n - j

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                result[i][j] = result[i + 1][j + 1]
            else:
                result[i][j] = 1 + min(result[i + 1][j], result[i][j + 1], result[i + 1][j + 1])

    return result[0][0]