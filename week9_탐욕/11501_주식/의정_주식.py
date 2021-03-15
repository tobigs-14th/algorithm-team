T = int(input())

for _ in range(T):
    N = int(input())
    value = list(map(int, input().split()))

    money = 0
    for i in range(N-1):
        max_price = max(value[i+1:])
        if value[i] < max_price:
            money += max_price - value[i]

    print(money)
