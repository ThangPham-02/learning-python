for _ in range(int(input())):
    p, q = input().split()
    x1 = input()
    if len(x1.split()) > 1:
        x1, x2 = x1.split()
    else:
        x2 = input()
    new_1 = int(x1.replace(p, q)) + int(x2.replace(p, q))
    new_2 = int(x1.replace(q, p)) + int(x2.replace(q, p))
    print(min(new_1, new_2), max(new_1, new_2))

