t = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    day = 0
    d = V//P
    day += L*d
    reminder = V%P
    if reminder >= L:
        day += L
    else:
        day += reminder
    print("Case {}: {}".format(t, day))
    t += 1
