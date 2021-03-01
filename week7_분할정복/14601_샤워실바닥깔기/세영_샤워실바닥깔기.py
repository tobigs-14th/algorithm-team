def check(size, x, y):
    for i in range(y, y+size):
        for j in range(x, x+size):
            if matrix[i][j] != 0:
                return False
    return True
            
def sol(size, x, y):
    global matrix
    global label
    label += 1
    s = size//2
    if check(s, x, y):matrix[y+s-1][x+s-1] = label
    if check(s, x, y+s):matrix[y+s][x+s-1] = label
    if check(s, x+s, y):matrix[y+s-1][x+s] = label
    if check(s, x+s, y+s):matrix[y+s][x+s] = label
    if s==1:return
    sol(s, x, y)
    sol(s, x+s, y)
    sol(s, x, y+s)
    sol(s, x+s, y+s)


K = int(input())
x, y = map(int, input().split())
matrix = [[0]*2**K for i in range(2**K)]
matrix[-y][x-1] = -1
    
label = 1
sol(2**K, 0, 0)
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
