n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

memo = [0 for _ in range(k+1)]
memo[0] = 1
for i in coin:
    for j in range(i, k+1):
        memo[j] += memo[j-i]

print(memo[k])
