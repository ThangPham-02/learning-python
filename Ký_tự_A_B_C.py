from itertools import combinations

N = input().split()
N, K = N[0], int(N[1])
A = list(map(int, input().split()))
filtered_A = []
for number in A:
    if str(number) not in filtered_A:
        filtered_A.append(str(number))
result = list(combinations(sorted(filtered_A), K))
for i in sorted(result):
    print(' '.join(i))
