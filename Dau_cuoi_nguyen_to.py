def so_nguyen_to(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for x in range(2, int(k ** 0.5)+1):
        if k % x == 0:
            return False
    return True

for i in range(int(input())):
    number = input()
    dau = number[:3]
    cuoi = number[-3:]
    if so_nguyen_to(int(dau)) and so_nguyen_to(int(cuoi)):
        print("YES")
    else:
        print("NO")
