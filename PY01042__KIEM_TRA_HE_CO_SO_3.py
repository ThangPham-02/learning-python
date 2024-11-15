def check(a, b):
    for x in a:
        if x not in b:
            return "NO"
    return "YES"

for _ in range(int(input())):
    string = input()
    N = ["0", "1", "2"]
    print(check(string, N))
