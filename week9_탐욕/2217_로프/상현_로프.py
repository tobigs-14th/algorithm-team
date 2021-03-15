N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort()

length = len(rope)
max_value = 0
for i in range(length):
    tmp = rope[i]
    tmp_value = tmp*(length-i)
    if max_value < tmp_value:
        max_value = tmp_value

print(max_value)
