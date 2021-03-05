T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int,input().split()))

    max_value = stock[-1]
    result = 0
    for i in range(len(stock)-1,-1, -1):
        if max_value >= stock[i]:
            result += max_value - stock[i]
        else:
            max_value = stock[i]
    print(result)
