N = int(input())
M = int(input())

button = {str(i) for i in range(10)}
if M != 0:
    button -= set(map(str, input().split()))
    
count = abs(N-100)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if num[j] not in button:break
        elif j == len(num)-1:
            count = min(count, abs(N-int(num)) + len(str(num)))

print(count)
