import math

N = int(input())
e = round(math.log(N,3))-1

star = ["***", "* *", "***"]
for i in range(e):
    matrix = []
    for i in range(3*len(star)):
        if i//len(star)==1:
            matrix.append(star[i%len(star)] + " "*len(star) + star[i%len(star)])
        else:
            matrix.append(star[i%len(star)]*3)
    star = matrix
            
for i in star:
    print(i)
