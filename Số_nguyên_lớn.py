def gcd(a, b):
    ucln = b % a
    if ucln == 0:
        return a
    else:
        return gcd(ucln, a)

for _ in range(int(input())):
    A = int(input())
    B = int(input())
    print(gcd(A, B))