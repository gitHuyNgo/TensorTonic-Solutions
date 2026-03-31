def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    result = []
    n = len(tokens)
    step = chunk_size - overlap

    for i in range(0, n, step):
        chunk = tokens[i : i + chunk_size]
        result.append(chunk)

        if i + chunk_size >= n:
            break

    return result