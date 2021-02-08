# 평범한 배낭

N, K = map(int, input().split())

item = []
for i in range(N):
    item.append(list(map(int, input().split())))

memo_value = [[0 for _ in range(K+1)] for _ in range(N+1)]

# i : item 번호
for i in range(1, N+1):
    # j : 최대 허용된 무게
    for j in range(1, K+1):
        if j - item[i-1][0] >= 0:
            memo_value[i][j] = max(memo_value[i-1][j-item[i-1][0]] + item[i-1][1], memo_value[i-1][j])
        else :
            memo_value[i][j] = memo_value[i-1][j]

print(memo_value[N][K])