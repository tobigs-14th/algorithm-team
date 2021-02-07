N = int(input())
memo = [i for i in range(N+1)]
for i in range(4, N+1):
    for j in range(int(i**0.5),0,-1):
        if i == j*j:
            memo[i] = 1
            break
        else:
            memo[i] = min(memo[i], memo[i-j*j]+1)
        
print(memo[-1])
