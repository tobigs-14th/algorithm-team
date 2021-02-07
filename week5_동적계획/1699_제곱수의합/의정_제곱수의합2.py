# 제곱수의 합2

import math

N = int(input())

rootN = int(math.sqrt(N))

memo = [0 for _ in range(N+1)]
for i in range(1, rootN+1):
    memo[i**2] = 1
    
for i in range(2, N+1):
    if memo[i] == 0:
        min_cnt = i
        rooti = int(math.sqrt(i))
        for j in range(2, rooti+1):
            min_cnt = min(min_cnt, memo[i - j**2]+1)
        memo[i] = min_cnt

print(memo[N])