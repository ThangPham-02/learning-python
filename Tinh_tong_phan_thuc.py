for _ in range(int(input())):
    N = int(input())
    total = 0
    if N % 2 == 0:
        for i1 in range(2, N + 2, 2):
            total += 1/i1
    else:
        for i2 in range(1, N + 2, 2):
            total += 1/i2
    print("{:.6f}".format(total))