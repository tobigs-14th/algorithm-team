# 포도주

def solution():
    global memo, wine, N
    memo[1] = wine[1]
    memo[2] = wine[1] + wine[2]
    for i in range(3, N+1):
        memo[i] = memo[i-1]
        memo[i] = max(memo[i], memo[i-2]+wine[i])
        memo[i] = max(memo[i], memo[i-3]+wine[i-1]+wine[i])

N = int(input())

wine = [0]+[int(input()) for _ in range(N)]+[0]
memo = [0 for _ in range(N+2)]

solution()

print(memo[N])