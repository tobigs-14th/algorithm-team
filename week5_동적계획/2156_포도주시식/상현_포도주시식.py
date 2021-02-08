n = int(input())
wine_list = [int(input()) for _ in range(n)]

if n <= 2:
    result = 0
    for i in range(n):
        result += wine_list[i]
    print(result)
else:
    dp = [0 for _ in range(len(wine_list))]
    dp[0] = wine_list[0]

    for i in range(1,len(dp)):
        dp[i] = max(dp[i-2] + wine_list[i], dp[i-3]+wine_list[i-1]+wine_list[i], dp[i-1])
    print(dp[-1])
