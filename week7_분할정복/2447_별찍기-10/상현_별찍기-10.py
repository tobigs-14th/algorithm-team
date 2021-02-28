N = int(input())

def hstack(*arrs):
    new = []
    a,b,c = arrs
    tmp = []
    for i in range(len(a)):
        tmp.extend(a[i])
        tmp.extend(b[i])
        tmp.extend(c[i])
        new.append(tmp)
        tmp = []
    return new

def vstack(*arrs):
    new = []
    for arr in arrs:
        new.extend(arr)
    return new

base = [[1,1,1],[1,0,1],[1,1,1]]

def recur(n):
    if n == 3:
        return base

    a = hstack(recur(n//3),recur(n//3),recur(n//3))
    jump = [[0 for _ in range(n//3)] for _ in range(n//3)]
    b = hstack(recur(n//3), jump, recur(n//3))
    c = hstack(recur(n//3),recur(n//3),recur(n//3))

    return vstack(a,b,c)

star_board = recur(N)

for i in star_board:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
