N, A = int(input()), list(map(int, input().split()))
count = 0
for i in range(0, N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            count += 1
print(count)