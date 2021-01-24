
# 백준 2961번 도영이가 만든 맛있는 음식

def mix(sour,bitter,s,b):
    global answer
    if len(sour) == 0:
        answer.append(abs(s-b))
        return
    
    for i in range(len(sour)):
        mix(sour[i+1:],bitter[i+1:],s,b)
        sTemp = s * sour[i]
        bTemp = b + bitter[i]
        mix(sour[i+1:],bitter[i+1:],sTemp,bTemp)
 
n = int(input())
sour = []
bitter = []
answer = []
for _ in range(n):
    s,b = map(int,input().split())
    sour.append(s)
    bitter.append(b)
 
for i in range(n):
    s = sour[i]
    b = bitter[i]
    mix(sour[i+1:],bitter[i+1:],s,b)
 
print(min(answer))
