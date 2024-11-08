def so_nguyen_to(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for x in range(2, int(k**0.5)+1):
        if k % x == 0:
            return False
    return True

for _ in range(int(input())):
    number = input()
    four_last_number = int(number[-4:])
    if so_nguyen_to(four_last_number):
        print('YES')
    else:
        print('NO')
