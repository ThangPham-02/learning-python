#trùng với bài Nguyên tố cùng nhau
def uc(a, b):
    ucln = b % a
    if ucln == 0:
        return a
    else:
        return uc(ucln, a)

n = int(input())
A = list(map(int, input().split()))
B = sorted(A)
for j in range(len(B)):
    for i in range(j+1, len(B)):
        if uc(B[j], B[i]) == 1:
            print(B[j], B[i])
