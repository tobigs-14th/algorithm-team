N, K = map(int, input().split())
things = [[0,0]]
for i in range(N):
    things.append(list(map(int, input().split())))

memo = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if things[i][0] > j:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(things[i][1] + memo[i-1][j-things[i][0]], memo[i-1][j])
            
print(memo[N][K])
