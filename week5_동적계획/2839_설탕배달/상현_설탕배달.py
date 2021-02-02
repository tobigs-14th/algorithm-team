def solve(N, dp_list):
    for i in range(t-1):
        dp_list[i+1][0] = dp_list[i][0] + 3
        for j in range(s-1):
            dp_list[i][j+1] = dp_list[i][j] + 5
            if dp_list[i][j] >N: break
            if dp_list[i][j] == N:
                return i+j

    return -1

N = int(input())

s,t = N//5 + 2, N //3 + 2

dp_list = [[0 for _ in range(s)] for _ in range(t)]
print(solve(N, dp_list))
