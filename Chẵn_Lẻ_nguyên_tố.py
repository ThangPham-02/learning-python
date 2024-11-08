# Kiểm tra số nguyên tố
def so_nguyen_to(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for x in range(2, int(k ** 0.5)):
        if k % x == 0:
            return False
    return True
# Kiểm tra vị trí chẵn là số chẵn, vị trí lẻ là số lẻ
def check_even_odd(even_odd):
    for i in range(len(even_odd)):
        if i % 2 == 0 and int(even_odd[i]) % 2 != 0:
            return False
        if i % 2 != 0 and int(even_odd[i]) % 2 == 0:
            return False
    return True

for _ in range(int(input())):
    N = input()
    total = 0
    for number in N:
        total += int(number)
    if check_even_odd(N) and so_nguyen_to(total):
        print("YES")
    else:
        print("NO")
