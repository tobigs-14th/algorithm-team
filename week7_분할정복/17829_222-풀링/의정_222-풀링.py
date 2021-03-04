def pooling(matrix, N):
    print(matrix)
    if N == 1:
        print(matrix[0][0])
        return
        
    new_matrix = []
    for i in range(0, N, 2):
        new_row = []
        for j in range(0, N, 2):
            tmp = [matrix[i][j], matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]]
            tmp.sort(reverse = True)
            new_row.append(tmp[1])
        new_matrix.append(new_row)
    pooling(new_matrix, int(N/2))
    
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

pooling(matrix, N)