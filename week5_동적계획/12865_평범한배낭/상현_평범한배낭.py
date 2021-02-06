N, K = map(int, input().split())
weights, values = [], []
for _ in range(N):
    w,v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    for j in range(1,K+1):
        weight = weights[i]
        value = values[i]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value+dp[i-1][j - weight], dp[i-1][j])

print(dp[-1][-1])
