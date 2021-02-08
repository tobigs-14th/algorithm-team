# 동전1 ver2

N, K = map(int, input().split())

value = [int(input()) for _ in range(N)]
dp = [0 for _ in range(K+1)]

dp[0] = 1
for i in value:
    for j in range(i, K+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
            
print(dp[K])