def so_nguyen_to(k):
    if k < 2:
        return "NO"
    if k == 2:
        return "YES"
    for x in range(2, int(k ** 0.5)):
        if k % x == 0:
            return "NO"
    return "YES"

for _ in range(int(input())):
    N = input()
    print(so_nguyen_to(int(N[-4:])))
