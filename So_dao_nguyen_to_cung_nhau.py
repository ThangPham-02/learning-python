def uc(a, b):
    ucln = b % a
    if ucln == 0:
        return a
    else:
        return uc(ucln, a)
for _ in range(int(input())):
    N = int(input())
    N_reversed = str(N)[::-1]
    if uc(N, int(N_reversed)) == 1:
        print("YES")
    else:
        print("NO")