def matrix_mul(a, b):
    result = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
    
    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
                
    return result

N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
tmp = result = matrix

B = bin(B)[2:] # 5 = 0b101

check = 1 if B[len(B)-1] == '1' else 0
for i in range(len(B)-2, -1, -1):
    # i번째에 해당하는 행렬 만들어주기
    tmp = matrix_mul(tmp, tmp)

    # i번째가 1이면 위 행렬 곱해주기
    if B[i] == '1':
        if check == 0:
            result = tmp
            check = 1 
        else :
            result = matrix_mul(result, tmp)

print(result)
