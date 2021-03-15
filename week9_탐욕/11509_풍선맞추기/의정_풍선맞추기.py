N = int(input())

H = list(map(int, input().split()))

arrow = 0
while True:
    height = max(H)
    index = H.index(height)

    if height == 0:
        break

    while height:
        H[index] = 0
        tmp = H[index+1:]
        height -= 1
        try:
            tmp_index = tmp.index(height)
            index = tmp_index + index + 1
        except:
            break
    arrow += 1

print(arrow)