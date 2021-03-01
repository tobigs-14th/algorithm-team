def star(x, y, N):
    if N >= 1 and x<original_N and y<original_N:
        for i in range(y, y+N):
            result[i] = result[i][:x] + list(' '*N) + result[i][x+N:]

        x1, x2, x3 = x-N//3*2, x+N//3, x+N+N//3
        y1, y2, y3 = y-N//3*2, y+N//3, y+N+N//3

        star(x1, y1, N//3)
        star(x2, y1, N//3)
        star(x3, y1, N//3)
        star(x1, y2, N//3)
        star(x3, y2, N//3)
        star(x1, y3, N//3)
        star(x2, y3, N//3)
        star(x3, y3, N//3)


N = int(input())   
result = [list('*'*N)]*N
original_N = N
star(N//3, N//3, N//3)

for i in range(N):
    print(''.join(result[i]))
