N = int(input())
M = int(input())
broken_list = list(input())


ans = 999999999
length = 0
for i in range(1000000):
    broken = False
    for s in str(i):
        if s in broken_list:
            broken = True

    if broken:
        continue
    else:
        if ans > abs(N-i):
            ans = abs(N-i)
            length = len(str(i))

ans = min(ans + length, abs(N-100))
print(ans)
