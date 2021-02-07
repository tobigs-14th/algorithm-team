n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

if n==1:
    print(wine[1])
else:
    memo = [0 for i in range(len(wine))]
    memo[1] = wine[1]
    memo[2] = wine[1] + wine[2]
    for i in range(3, len(memo)):
        memo[i] = max(memo[i-1], memo[i-2]+wine[i], memo[i-3]+wine[i-1]+wine[i])

    print(memo[n])
