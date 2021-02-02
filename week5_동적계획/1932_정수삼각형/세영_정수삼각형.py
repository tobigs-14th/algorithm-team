n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

memo = [t.copy() for t in triangle]
memo[1] = [memo[0][0]+i for i in memo[1]]

for i in range(2, n):
    for j in range(i+1):
        if j==0:
            memo[i][j] += memo[i-1][0]
        elif j==i:
            memo[i][j] += memo[i-1][i-1]
        else:
            memo[i][j] += max(memo[i-1][j-1], memo[i-1][j])
        
print(max(memo[-1]))
