def check_nguyen_to(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for item in range(2, int(number ** 0.5)+1):
        if number % item == 0:
            return False
    return True

def check(a):
    a1 = a + 2
    a2 = a + 4
    a3 = a + 6
    if check_nguyen_to(a2) and check_nguyen_to(a3):
        return True
    if check_nguyen_to(a1) and check_nguyen_to(a3):
        return True
    return False

for _ in range(int(input())):
    N = int(input())
    count = 0
    for i in range(2, N-6):
        if check_nguyen_to(i) and check(i):
            count += 1
    print(count)
