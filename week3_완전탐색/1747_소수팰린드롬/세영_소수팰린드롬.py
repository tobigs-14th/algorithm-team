
# 1747 소수&팰린드롬

N = int(input())

for i in range(N, 1050000):
    breaker = True
    
    for j in range(2, int(i**0.5)+1): # 소수
        if i%j == 0:
            breaker = False
            break
    
    if breaker:
        i_str = str(i)
        if i_str != i_str[::-1]:
            breaker = False
        
    if breaker:break

if N==1:print(2)
else:print(i)


