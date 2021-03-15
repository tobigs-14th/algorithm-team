N = int(input())
H = list(map(int, input().split()))

height = [0 for _ in range(1000001)]
arrow = 0
for h in H:
    if height[h+1] == 0:
        height[h] += 1
        arrow += 1
    else:
        height[h+1] -= 1
        height[h] += 1
    
print(arrow)
