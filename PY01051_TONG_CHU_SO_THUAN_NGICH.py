for _ in range(int(input())):
    N = input()
    total = 0
    for i in N:
        total += int(i)
    if str(total) == str(total)[::-1] and len(str(total)) > 1:
        print("YES")
    else:
        print("NO")