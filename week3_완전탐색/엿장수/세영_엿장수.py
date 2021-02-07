n,c,f = map(int, input().split())
size = []
for i in range(n):
    size.append(int(input()))

max_size = max(size)

optimal = 0

for i in range(1,max_size+1):
    count = [s//i for s in size]
    cutting_count = []
    for j in range(len(size)):
        if size[j]>=i:
            if (size[j]%i)==0:cutting_count.append(count[j]-1)
            else:cutting_count.append(count[j])
        else:cutting_count.append(0)
    optimal = max(optimal, i*sum(count)*f-c*sum(cutting_count))

print(optimal)
