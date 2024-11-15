def so_nguyen_to(k):
    if k < 2:
        return "NO"
    if k == 2:
        return "YES"
    for x in range(2, int(k ** 0.5)+1):
        if k % x == 0:
            return "NO"
    return "YES"

for i in range(int(input())):
    number = int(input())
    total = 0
    for a in str(number):
        total += int(a)
    print(so_nguyen_to(total))

