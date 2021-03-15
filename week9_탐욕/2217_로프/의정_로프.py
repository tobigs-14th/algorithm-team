N = int(input())

rope = [int(input()) for _ in range(N)]

rope.sort()

max_weight = 0
for i in range(N):
    weight = rope[i] * (N-i)
    max_weight = weight if max_weight < weight else max_weight

print(max_weight)