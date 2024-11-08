def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    N = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    print(check(A, B))
