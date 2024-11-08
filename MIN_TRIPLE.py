def sum_(a, t):
    for count in range(3):
        t += min(a)
        a.remove(min(a))
    return t

for _ in range(int(input())):
    N, A = int(input()), list(map(int, input().split()))
    total = 0
    print(sum_(A, total))
