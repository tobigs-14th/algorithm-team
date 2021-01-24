from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]


home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

small = float('inf')
for cases in combinations(chicken, M):
    tmp = 0
    for h in home:
        tmp_list = []
        for case in cases:
            tmp_list.append(abs(case[0]-h[0])+abs(case[1]-h[1]))
        tmp += min(tmp_list)

    if tmp < small:
        small = tmp

print(small)
