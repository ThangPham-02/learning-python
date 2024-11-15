for _ in range(int(input())):
    N = input()
    cal = 1
    for i in N:
        if i != "0":
            cal *= int(i)
    print(cal)
