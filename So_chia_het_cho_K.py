a, K, N = map(int,input().split())
list_b = []
i = K - a % K
N = N - a
while i <= N:
    list_b.append(i)
    i += K
if len(list_b) == 0:
    print(-1)
else:
    for i in list_b:
        print(i, end = " ")

