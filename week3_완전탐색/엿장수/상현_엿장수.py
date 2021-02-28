N,C,F = map(int,input().split()) #N = 엿가락의 개수, C=자를때 비용, F=엿 한 가락의 가격

L_list = [int(input()) for _ in range(N)]
max_lenght = max(L_list)
earn_list = []
for i in range(1,max_lenght+1):
    cost = 0
    for j in L_list:
        n = j//i
        if (j/i)%1 == 0:
            cut_count = n-1
        else:
            cut_count = n

        cost += n*i*F - cut_count*C
    earn_list.append(cost) #길이별 가격을 리스트에 추가

print(max(earn_list)) #가장 큰 값을 출력
