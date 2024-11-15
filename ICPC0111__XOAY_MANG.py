for _ in range(int(input())):
    length, d = input().split()
    A = list(map(int, input().split()))
    new = A[int(d):] + A[:int(d)]
    print(*new)