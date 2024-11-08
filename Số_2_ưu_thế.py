def check(a, b):
    for x in a:
        if x not in b:
            return False
    return True

for _ in range(int(input())):
    number = int(input())
    include = ["0", "1", "2"]
    result = []
    i = 2
    while number > 0:
        if str(i).count("2") > len(str(i)) / 2 and check(str(i), include):
            result.append(i)
            number -= 1
        i += 1
    print(*result)
