# 제곱수의 합

import math

def find_cnt(N, rootN):
    if N == 1:
        return 1
    
    global memo
    
    min_cnt = N
    for i in range(2, rootN+1):
        check_num = N - i**2
        if memo[check_num] == 0:
            memo[check_num] = find_cnt(check_num, int(math.sqrt(check_num)))
            
        min_cnt = min(min_cnt, memo[check_num])
        
    return min_cnt + 1

N = int(input())

rootN = int(math.sqrt(N))
memo = [0 for _ in range(N+1)]
for i in range(1, rootN+1):
    memo[i**2] = 1
    
answer = find_cnt(N, rootN)

print(int(answer))

