def change_location(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
    else:
        change_location(n-1, a, c, b)
        change_location(1, a, b, c)
        change_location(n-1, b, a, c)

N = int(input())
rod_1 = "A"
rod_2 = "B"
rod_3 = "C"
change_location(N, rod_1, rod_2, rod_3)
