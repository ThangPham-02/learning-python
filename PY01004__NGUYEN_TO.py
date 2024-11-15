# Tìm ucln
def gcd(a,b):
    ucln = b % a
    if ucln == 0:
        return a
    if a == b:
        return a
    if a % ucln == 0:
        return ucln
    else:
        return gcd(ucln,a)
# Kiểm tra K có là số nguyên tố không
def so_nguyen_to(k):
    if k < 2:
        return "NO"
    if k == 2:
        return "YES"
    for x in range(2, int(k ** 0.5)):
        if k % x == 0:
            return "NO"
    return "YES"

test = int(input())
for _ in range(test):
    N = int(input())
    K = 0
    for i in range(1, N):
        gcd(i, N)
        if gcd(i, N) == 1:
            K += 1
    print(so_nguyen_to(K))

