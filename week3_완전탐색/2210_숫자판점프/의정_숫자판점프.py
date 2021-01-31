# https://www.acmicpc.net/problem/2210

# 2210번 숫자판 점프
def dfs(x, y, number):
    if len(number) == 8: #8자리 숫자가 만들어졌다면
        if number not in result: #result에 없다면
            result.append(number)
        return
        
    dx = [1, -1, 0, 0] #상하좌우 확인 x
    dy = [0, 0, 1, -1] #상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 4 and 0 <= ddy < 4: #범위 내에 있다면
            dfs(ddx, ddy, number + matrix[ddx][ddy]) #8글자가 될 때 까지 재귀

#입력
matrix = [list(map(str, input().split())) for _ in range(4)]

result = []
for i in range(4):
    for j in range(4):
        dfs(i, j, matrix[i][j]) #0,0부터 3,3까지 모두 검사
# print(result)
print(len(result))