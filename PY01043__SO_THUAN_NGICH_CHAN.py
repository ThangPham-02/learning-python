def check(a):
    for b in str(a):
        if int(b) % 2 != 0:
            return False
    return True

result = []
num = 2
while num <= 888:
    if check(num):
        temp = str(num)
        result.append(int(temp + temp[::-1]))
    num += 2
for _ in range(int(input())):
    number = int(input())
    for i in result:
        if i >= number:
            break
        else:
            print(i, end = ' ')
    print('')