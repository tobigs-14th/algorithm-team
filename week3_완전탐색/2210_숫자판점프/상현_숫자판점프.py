board = [input().split() for _ in range(5)]

def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for k in range(4):
        next_x = x+dx[k]
        next_y = y+dy[k]

        if 0 <= next_x <= 4 and 0 <= next_y <= 4:
            dfs(next_x, next_y, number+board[next_x][next_y])


result = []
for i in range(5):
    for j in range(5):
        dfs(i,j, board[i][j])
print(len(result))
