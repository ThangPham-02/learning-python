# Hàm kiểm tra số nguyên tố
def check_nguyen_to(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for item in range(2, int(number ** 0.5)+1):
        if number % item == 0:
            return False
    return True
# Kiểm tra số nguyên tố của N, N đảo, tổng chữ số của N, từng chữ số của N
def check_conditions(a0, a1, b, c):
    if not(check_nguyen_to(a0)):
        return False
    if not(check_nguyen_to(a1)):
        return False
    if not(check_nguyen_to(b)):
        return False
    for num in c:
        if not(check_nguyen_to(int(num))):
            return False
    return True

for _ in range(int(input())):
    perfect_number = input()
    reversed_perfect_number = perfect_number[::-1]
    total = 0
    for i in perfect_number:
        total += int(i)
    if check_conditions(int(perfect_number), int(reversed_perfect_number), total, perfect_number):
        print("Yes")
    else:
        print("No")
