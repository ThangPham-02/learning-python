def check(a):
    for b in a:
        if int(b) % 2 != 0:
            return False
    return True
result = []
num = 2
while num <= 888:
    if check(str(num)):
        temp = str(num)
        result.append(int(temp + temp[::-1]))
    num += 2

test = int(input())
while test > 0:
    number = int(input())
    for i in result:
        if i >=number:
            break
        print(i, end = ' ')
    print('')
    test -= 1


##Cách 1:
# def check(a, b, c):
#     if c % 2 != 0:
#         return False
#     for x in a:
#         if x not in b:
#             return False
#     return True
# # a = str(i)
# # b = list_number
# # c = len(str(i))
# for _ in range(int(input())):
#     number = int(input())
#     list_number = ["0", "2", "4", "6", "8"]
#     result = []
#     for i in range(22,number):
#         if str(i) == str(i)[::-1] and i % 2 == 0:
#             if check(str(i), list_number, len(str(i))):
#                 result.append(i)
#     print(*result)

