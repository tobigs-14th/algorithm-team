
# 2210 숫자판 점프

def make_nums(x, y, num):
    global nums
    
    if len(num)==6:
        if num not in nums:
            nums.append(num)
        return

    dxdy = [[1,0], [-1,0], [0,1], [0,-1]]
    
    for dx, dy in dxdy:
        _x = x + dx
        _y = y + dy
        
        if 0<=_x<5 and 0<=_y<5:
            make_nums(_x, _y, num+board[_x][_y])


board = []
for i in range(5):board.append(list(input().split()))

nums = []
            
for i in range(5):
    for j in range(5):
        make_nums(i, j, board[i][j])
        
print(len(nums))

