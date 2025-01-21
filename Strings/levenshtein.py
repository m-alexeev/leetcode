def minDistance(w1: str, w2: str) -> int:
    M = len(w1)
    N = len(w2)
    d = [[0] * (N + 1) for _ in range(M + 1)]
    if M == N == 0:
        return 0
    if M == 0 and N > 0:
        return N
    if N == 0 and M > 0:
        return M

    for i in range(M + 1):
        d[i][0] = i
    for j in range(N + 1):
        d[0][j] = j

    i = 1
    while i < M + 1:
        j = 1
        while j < N + 1:
            if w1[i - 1] == w2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
            j += 1
        i += 1
    print(d)

    return d[M][N]


print(minDistance("horse", "ros"))
