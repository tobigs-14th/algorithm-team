T = int(input())
jusiks = []
for i in range(T):
    N = int(input())
    jusiks.append(list(map(int, input().split())))

for jusik in jusiks:
    profit = 0
    highest = 0
    for i in range(len(jusik)-1, -1, -1):
        if jusik[i] > highest:
            highest = jusik[i]
        else:
            profit += highest - jusik[i]
    print(profit)
