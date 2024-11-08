#Tìm ucln
def uc(a, b):
    ucln = b % a
    if ucln == 0:
        return a
    else:
        return uc(ucln, a)
#Kiểm tra số nguyên tố
def so_nguyen_to(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for x in range(2, int(k**0.5)+1):
        if k % x == 0:
            return False
    return True

for i in range(int(input())):
    A, B = map(int, input().split())
    number = uc(A, B)
    total = 0
    for item in str(number):
        total += int(item)
    if so_nguyen_to(total):
        print("YES")
    else:
        print("NO")
