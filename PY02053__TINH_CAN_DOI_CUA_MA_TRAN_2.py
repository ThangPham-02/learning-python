N = int(input())
matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row[::-1])
K = int(input())
sum_above = 0
sum_under = 0
for a in range(N):
    for b in range(N):
        if a < b:
            sum_above += matrix[a][b]
        if a > b:
            sum_under += matrix[a][b]
if abs(sum_above - sum_under) <= K:
    print("YES")
else:
    print("NO")
print(abs(sum_above - sum_under))