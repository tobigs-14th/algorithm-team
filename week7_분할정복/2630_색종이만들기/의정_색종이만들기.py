white_num = 0
blue_num = 0
def check_paper(x, y, N):
    global paper, white_num, blue_num

    hap = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            hap += paper[i][j]

    if hap == 0:
        white_num += 1
        return
    elif hap == N**2:
        blue_num += 1
        return

    half = int(N/2)
    check_paper(x, y, half)
    check_paper(x + half, y, half)
    check_paper(x, y + half, half)
    check_paper(x + half, y + half, half)

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

check_paper(0, 0, N)

print(white_num)
print(blue_num)