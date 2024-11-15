def check(a):
    if len(a) < 3:
        return "NO"
    i = 0
    while i < len(a) - 1 and a[i] < a[i+1]:
        i += 1
    while i < len(a) - 1 and a[i] > a[i+1]:
        i += 1
    if i ==  len(a) - 1:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    number = input()
    print(check(number))
