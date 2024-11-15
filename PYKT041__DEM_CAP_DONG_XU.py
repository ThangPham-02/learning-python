N = int(input())
A = []
for i in range(N):
    A.append(input())
count = 0
for a in range(N):
    for b in range(N):
        if A[a][b] == "C":
            for c in range(b+1, N):
                if A[a][c] == "C":
                    count += 1
            for d in range(a+1, N):
                if A[d][b] == "C":
                    count += 1
print(count)