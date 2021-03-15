N = int(input())
balloon = list(map(int, input().split()))

st = [0 for _ in range(1000001)]
cnt = 0

for i in range(N):
    ins = balloon[i]
    if(st[ins+1] == 0):
        st[ins] += 1
        cnt += 1
        continue
    st[ins+1] -= 1
    st[ins] += 1
print(cnt)
