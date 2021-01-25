from itertools import combinations

N, M = map(int, input().split())

number = list(map(int, input().split()))

answer = 0
for cards in combinations(number, 3):
    total = sum(cards)
    if total <= M:
        if answer < total:
            answer = total

print(answer)