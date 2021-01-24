N = int(input())

def eratos(n):
    a = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

prime_list = eratos(1005000)
num_list = [i for i in prime_list if i >= N]

str_number = list(map(str, num_list))

for checks in str_number:
    if checks == checks[::-1]:
        print(int(checks))
        break
