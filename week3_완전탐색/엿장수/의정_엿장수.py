N, C, F = list(map(int, input().split()))

yuts = []
for i in range(N):
    yuts.append(int(input()))
    
max_price = 0
for yut_len in range(1, max(yuts)):
    price = 0
    for yut in yuts:
        price += (yut-(yut%yut_len))*F
        price -= (yut//yut_len)*C
        if max_price < price:
            max_price = price
            
print(max_price)