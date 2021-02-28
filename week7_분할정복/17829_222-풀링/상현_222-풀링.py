def solve(arr):
    n = len(arr)
    inter = []
    for i in range(0,n,2):
        row2 = arr[i:i+2]
        tmp = []
        for j in range(0, n, 2):
            current = row2[0][j:j+2]
            current.extend(row2[1][j:j+2])
            current.sort()
            tmp.append(current[-2])
        inter.append(tmp)
    return inter


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
result = solve(mat)
while len(result) != 1:
    result = solve(result)
print(result[0][0])
