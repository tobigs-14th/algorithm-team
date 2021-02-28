N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


def row(arr):
    result = []
    n = len(arr)
    step = int(n**0.5)
    for i in range(0,n, step):
        result.append(arr[i:i+step])
    return result

def devide(arr):
    n = len(arr)
    arr1, arr2, arr3, arr4 = [],[],[],[]
    for i in range(n):
        for j in range(n):
            if i < n//2 and j < n//2:
                arr1.append(arr[i][j])
            elif i >= n//2 and j < n//2:
                arr2.append(arr[i][j])
            elif i >= n//2 and j >= n//2:
                arr3.append(arr[i][j])
            else:
                arr4.append(arr[i][j])
    arr1 = row(arr1)
    arr2 = row(arr2)
    arr3 = row(arr3)
    arr4 = row(arr4)
    return arr1, arr2, arr3, arr4

def isfull(arr):
    n = len(arr)
    sum_blocks = 0
    for i in range(n):
        sum_blocks += sum(arr[i])
    if sum_blocks == n**2:
        return 'blue'
    elif sum_blocks == 0:
        return 'white'
    return False

def recur(arr):
    global blue
    global white
    if isfull(arr) == 'blue':
        blue += 1
        return
    elif isfull(arr) == 'white':
        white += 1
        return

    arr1, arr2, arr3, arr4 = devide(arr)
    recur(arr1)
    recur(arr2)
    recur(arr3)
    recur(arr4)
    return

blue, white = 0, 0
recur(paper)
print(white)
print(blue)
