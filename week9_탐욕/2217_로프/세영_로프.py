N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

weight = 0
rope.sort()
for i in range(N):
    weight = max(weight, rope[i] * (N - i))
print(weight)
