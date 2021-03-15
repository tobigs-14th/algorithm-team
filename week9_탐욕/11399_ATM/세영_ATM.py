N = int(input())
P = list(map(int, input().split()))

P.sort()
waiting = 0
tmp = 0
for p in P:
    tmp += p
    waiting += tmp
print(waiting)
