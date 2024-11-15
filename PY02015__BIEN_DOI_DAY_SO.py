def check(a, cnt):
    b = []
    for i in range(len(a) - 1):
        b.append(abs(a[i] - a[i+1]))
        if i == 2:
            b.append(abs(a[3] - a[0]))
    if b == [0, 0, 0, 0]:
        return cnt
    else:
        cnt += 1
        return check(b, cnt)

while 1:
    A = list(map(int, input().split()))
    if A == [0, 0, 0, 0]:
        break
    count = 0
    print(check(A, count))
