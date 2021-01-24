from itertools import combinations

N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]
ingredients

def cal(arr):
    s_list = [a[0] for a in arr]
    b_list = [a[1] for a in arr]
    s = 1
    for i in s_list:
        s *= i
    b = 0
    for i in b_list:
        b += i

    return abs(s-b)

diff = float('inf')
for i in range(1,N+1):
    for case in combinations(ingredients, i):
        tmp = cal(case)
        if tmp < diff:
            diff = tmp

print(diff)
