N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

def pooling(matrix):
    if len(matrix) == 2:
        return sorted(sum(matrix, []))[-2]
    
    quadrant1 = [m[:len(matrix)//2] for m in matrix[:len(matrix)//2]]
    quadrant2 = [m[len(matrix)//2:] for m in matrix[:len(matrix)//2]]
    quadrant3 = [m[:len(matrix)//2] for m in matrix[len(matrix)//2:]]
    quadrant4 = [m[len(matrix)//2:] for m in matrix[len(matrix)//2:]]

    return pooling([[pooling(quadrant1), pooling(quadrant2)], [pooling(quadrant3), pooling(quadrant4)]])
    
print(pooling(matrix))
