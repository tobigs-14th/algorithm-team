N, M, K = map(int, input().split())

num = list(map(int, input().split()))

num.sort(reverse=True)

result = num[0] * K * M//(K+1) + num[1] * M//(K+1) + num[0] * M % (K+1)
print(result)