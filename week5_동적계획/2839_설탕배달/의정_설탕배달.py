# 설탕배달

N = int(input())

answer = -1
for i in range(N//5, -1, -1):
    if (N - i*5) % 3 == 0 :
        answer = i + (N - i*5) // 3
        break

print(answer)