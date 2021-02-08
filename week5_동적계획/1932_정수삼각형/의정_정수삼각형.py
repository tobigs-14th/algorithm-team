# 정수 삼각형

N = int(input())

triangle = []
memo_triangle = []
for i in range(N):
    triangle.append(list(map(int, input().split())))
    memo_triangle.append([0 for _ in range(len(triangle[i]))])
        
for i in range(N):
    for j in range(i+1):
        left = memo_triangle[i-1][j-1] if (i-1 >= 0) and (j-1 >= 0) else 0
        right = memo_triangle[i-1][j] if (i-1 >= 0) and (j < i) else 0
        
        memo_triangle[i][j] = triangle[i][j] + max(left, right)

print(max(memo_triangle[N-1]))