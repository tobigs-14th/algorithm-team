n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


dp = [0 for i in range(k+1)]
dp[0] = 1
for i in coins:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
        print(j, dp)

dp
