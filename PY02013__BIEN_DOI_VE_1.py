def check(n, cnt):
    cnt += 1
    if n == 1:
        return cnt
    if n % 2 == 0:
        return check(n / 2, cnt)
    if n % 2 != 0:
        return check(n * 3 +1, cnt)

while 1:
    number = int(input())
    count = 0
    if number == 0:
        break
    else:
        print(check(number, count))
