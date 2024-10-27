test = int(input())
for i in range(test):
    N, X, M = map(float,input().split())
    for x in range(1,100000):
        new = N * ((1+X/100) ** x)
        if new >= M:
            print(x)
            break
