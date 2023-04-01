def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    Path = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                Path[i][w] = 0
            elif wt[i - 1] <= w:
                if val[i - 1] + K[i - 1][w - wt[i - 1]] < K[i - 1][w]:
                    K[i][w] = K[i - 1][w]
                    Path[i][w] = 1
                else:
                    K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                    Path[i][w] = 2
            else:
                K[i][w] = K[i - 1][w]
                Path[i][w] = 0


    Path2 = [0 for x in range(n)]
    i = n
    w = W
    while i > 0:
        if Path[i][w] == 0:
            Path2[i - 1] = 0
            i = i - 1
        elif Path[i][w] == 1:
            Path2[i - 1] = 0
            i = i - 1
        else:
            Path2[i-1] = 1
            w = w - wt[i-1]
            i = i - 1
    return Path2


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))