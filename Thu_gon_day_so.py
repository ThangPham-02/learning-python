N = int(input())
A = list(map(int, input().split()))
res = []
for i in A:
    if len(res) == 0:
        res.append(i)
    else:
        if (res[-1] + i) % 2 != 0:
            res.append(i)
        else:
            res.pop(-1)
print(len(res))

