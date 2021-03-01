N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(lambda x:x%1000, map(int, input().split()))))

def mul(R,C):
    result = []
    for r in range(len(R)):
        tmp = []
        for c in range(len(C)):
            tmp.append(sum(list(map(lambda x,y:x*y%1000, R[r], [i[c] for i in C]))))
        result.append(tmp)
    return result

def square(A, B):
    if B == 1:
        return A
    if B == 2:
        return mul(A, A)
    if B % 2 > 0:
        return mul(square(A, B-1), A)
    else:
        tmp = square(A, B//2)
        return mul(tmp, tmp)
    
for i in square(A, B):
    for j in i:
        print(j%1000, end = ' ')
    print()
