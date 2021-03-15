N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
first, second = nums[0], nums[1]
if first > second:
    result = (first * K + second) * M // (K+1) + first * (M % (K+1))
else:
    result = first * M
print(result)
