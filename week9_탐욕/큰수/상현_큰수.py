N, M, K = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()

result = 0
cnt = 0
for i in range(M):
    if cnt < K:
        big = max(number_list)
        cnt += 1
    else:
        big = max(number_list[:-1])
        cnt = 0
    result += big

print(result)
