def wagner_fisher(seq1, seq2):
    m, n = len(seq1), len(seq2)
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # Initialize the first row and column
    for i in range(m+1):
        D[i][0] = i
    for j in range(n+1):
        D[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                subCost = 0
            else:
                subCost = 3
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + subCost)

    # The bottom-right cell contains the minimum edit distance
    return D[m][n]
