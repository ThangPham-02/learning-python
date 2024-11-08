def check(a):
    cnt = 0
    for i in range(1, a+1):
        if a % i == 0:
            cnt += 1
    if cnt == 9:
        return True
    else:
        return False

number = int(input())
count = 0
for num in range(1, number + 1):
    if check(num):
        count += 1
print(count)