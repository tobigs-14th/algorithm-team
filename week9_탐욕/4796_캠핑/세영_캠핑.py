camping = []
while True:
    lpv = list(map(int, input().split()))
    camping.append(lpv)
    if sum(lpv) == 0:
        break

num = 1
for c in camping[:-1]:
    l, p, v = c
    camp = v // p * l
    camp += min(v % p, l)
    print('Case %d: %d' %(num, camp))
    num += 1
