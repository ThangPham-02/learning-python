from collections import Counter

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    frequency = Counter(A)
    for i in frequency:
        if frequency[i] % 2 != 0:
            print(i)
            break