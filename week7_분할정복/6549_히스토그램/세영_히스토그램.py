def biggest(height):
    global area
    min_index = height.index(min(height))
    area = max(height[min_index]*len(height), area)
    
    left, right = height[:min_index], height[min_index+1:]
    if len(left)>=1:biggest(left)
    if len(right)>=1:biggest(right)


area = 0
n = int(input())
case = list(map(int, input().split()))

biggest(case)
print(area)
