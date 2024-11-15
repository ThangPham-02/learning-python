def so_nguyen_to(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for x in range(2, int(k**0.5)+1):
        if k % x == 0:
            return False
    return True
# kiểm tra phần tử ở vị trí nguyên tố là số nguyên tố, ngược lại
def check(num):
    for i in range(len(num)):
        if so_nguyen_to(i) and not(so_nguyen_to(int(num[i]))):
            return False
        if not(so_nguyen_to(i)) and so_nguyen_to(int(num[i])):
            return False
    return True

for _ in range(int(input())):
    number = input()
    if check(number):
        print("YES")
    else:
        print("NO")
