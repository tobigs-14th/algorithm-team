N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

def quadrant(P):
    global white, blue
    if sum([sum(p) for p in P]) == 0:
        white += 1
    elif sum([sum(p) for p in P]) == len(P)**2:
        blue += 1
    else:
        quadrant([p[:len(P)//2] for p in P[:len(P)//2]])
        quadrant([p[len(P)//2:] for p in P[:len(P)//2]])
        quadrant([p[:len(P)//2] for p in P[len(P)//2:]])
        quadrant([p[len(P)//2:] for p in P[len(P)//2:]])
        
white, blue = 0, 0
quadrant(paper)
print(white)
print(blue)
