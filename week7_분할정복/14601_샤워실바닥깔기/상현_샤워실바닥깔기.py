k = int(input())
raw_x,raw_y = map(int, input().split())
x,y = (2**k)-raw_y, raw_x - 1

board = [[0 for _ in range(2**k)] for _ in range(2**k)]
tile = 1



def color(x_start, x_end, y_start, y_end, x, y):
    global board
    global tile

    if x_end - x_start == 1 or y_end - y_start == 1:
        return
    half_x, half_y = (x_end + x_start)//2, (y_end + y_start)//2

    if x_start <= x < half_x and y_start <= y < half_y:
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if i >= half_x or j >= half_y:
                    board[i][j] = tile
        tile += 1
        color(x_start, half_x, half_y, y_end, half_x-1, half_y)
        color(half_x, x_end, y_start, half_y, half_x, half_y - 1)
        color(half_x, x_end, half_y, y_end, half_x, half_y)
        color(x_start, half_x, y_start, half_y, x, y)

    elif x_start <= x < half_x and half_y <= y < y_end:
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if i >= half_x or j < half_y:
                    board[i][j] = tile
        tile += 1
        color(x_start, half_x, y_start, half_y, half_x-1, half_y-1)
        color(half_x, x_end, y_start, half_y, half_x, half_y-1)
        color(half_x, x_end, half_y, y_end, half_x, half_y)
        color(x_start, half_x, half_y, y_end, x, y)

    elif half_x <= x < x_end and y_start <= y < half_y:
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if i < half_x or j >=half_y:
                    board[i][j] = tile
        tile += 1
        color(x_start, half_x, y_start, half_y, half_x-1, half_y-1)
        color(x_start, half_x, half_y, y_end, half_x-1, half_y)
        color(half_x, x_end, half_y, y_end, half_x, half_y)
        color(half_x, x_end, y_start, half_y, x, y)

    elif half_x <= x < x_end and half_y <= y < y_end:
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if i < half_x or j < half_y:
                    board[i][j] = tile
        tile += 1
        color(x_start, half_x, y_start, half_y, half_x-1, half_y-1)
        color(x_start, half_x, half_y, y_end, half_x-1, half_y)
        color(half_x, x_end, y_start, half_y, half_x, half_y-1)
        color(half_x, x_end, half_y, y_end, x, y)

color(0,2**k,0,2**k,x,y)

board[x][y] = -1
length = len(board)
for i in range(length):
    for j in range(length):
        if j != length-1:
            print(board[i][j], end = ' ')
        else:
            print(board[i][j])
