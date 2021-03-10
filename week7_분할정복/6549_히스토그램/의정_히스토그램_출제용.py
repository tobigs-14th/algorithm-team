def big_square(start, end):
    global hist

    if end-start == 1:
        answer = hist[start]
        return answer

    half = int((start + end)/2)
    #left
    left = big_square(start, half)
    #mid
    midl, midr, width = half-1, half, 2
    mid = min(hist[midl], hist[midr]) * width
    while True:
        if midl-1 < start:
            break

        midl -= 1
        width += 1

        new_mid = min(hist[midl:midr+1]) * width

        if mid > new_mid:
            midl += 1
            width -= 1
            break

        mid = new_mid

    while True:
        if midr+1 >= end:
            break
        
        midr += 1
        width += 1
        new_mid = min(hist[midl:midr+1]) * width

        if mid > new_mid:
            midr -= 1
            width -= 2
            break

        mid = new_mid

    #right
    right = big_square(half, end)
    
    answer = max([left, right, mid])
    return answer

num = int(input())
hist = [int(input()) for _ in range(num)]

answer = big_square(0, num)

print(answer)


