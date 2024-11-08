def uc(a, b):
    ucln = b % a
    if ucln == 0:
        return a
    else:
        return uc(ucln, a)

N, K = map(int, input().split())
new_list = []
for number in range(10**(K-1), 10**K):
    if len(str(number)) == K and uc(number, N) == 1:
        new_list.append(number)
new_list.sort()
for index in range(0, len(new_list), 10):
    print(*new_list[index:index +10])
