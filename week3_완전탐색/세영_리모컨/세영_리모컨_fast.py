def check(num):
    length = len(num)
    #if length == 0: return "9999999"
    small = list(filter(lambda x: x in use, num_list[0: int(num[0])]))  # 첫자리수보다 작은 버튼
    big = list(filter(lambda x: x in use, num_list[int(num[0]) + 1: 10]))  # 첫자리수보다 큰 버튼
    a = small[-1] + use[-1] * (length - 1) if len(small) else "9999999"  # small 첫자리수 중에 가장 큰 수
    b = num[0] if length == 1 and num[0] in use else num[0] + check(num[1:]) if num[0] in use else "9999999"  # 재귀
    c = big[0] + use[0] * (length - 1) if len(big) else "9999999"  # big 첫자리수 중에 가장 작은 수
    abcde = [a, b, c]
    if length == len(n):
        d = use[-1] * (length - 1) if len(use) and length >= 2 else "9999999"  # 자리수 자체가 하나 작은 수 중에 가장 큰 수
        e = ((use[0] if use[0] != '0' else use[1] if len(use) > 1 else "9999999") + use[0] * length) if len(use) else "9999999"  # 자리수 자체가 하나 큰 수 중에 가장 작은 수
        abcde += [d, e]
    abcde.sort(key=lambda x: len(x))
    abs_num = list(map(lambda x: abs(int(num) - int(x)), abcde))
    return str(abcde[abs_num.index(min(abs_num))])

n = input()
broken = list(input().split()) if int(input()) else []
num_list = list(map(str, range(10)))
use = list(filter(lambda x: x not in broken, num_list))
near_num = check(n)
print(min(abs(int(n) - int(near_num)) + len(near_num), abs(100 - int(n))))
