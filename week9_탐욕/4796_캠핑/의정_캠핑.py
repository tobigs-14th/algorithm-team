case = 1
while True:
    L, P, V = map(int, input().split())

    if (L + P + V) == 0:
        break

    day = V // P * L + min(V % P, L)

    print(f'Case {case}: {day}')
    case += 1