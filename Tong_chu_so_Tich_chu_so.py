# Cách 1: dùng enumerate
# test = int(input())
# for i in range(test):
#     n = int(input())
#     N = []
#     for x in str(n):
#         N.append(int(x))
#     total = 0
#     mul = 1
#     for index, number in enumerate(N):
#         if index % 2 == 0:
#             total += number
#         if index % 2 != 0 and number != 0:
#             mul *= number
#     if mul == 1:
#         mul = 0
#     print(total, mul)
# Cách 2: không cần hàm enumerate
test = int(input())
for i in range(test):
    n = int(input())
    N = []
    for x in str(n):
        N.append(int(x))
    N_even = []
    N_odd = []
    for item in range(0,len(N)):
        if item % 2 == 0:
            N_even.append(N[item])
        if item % 2 != 0 and N[item] != 0:
            N_odd.append(N[item])
    total = 0
    cal = 1
    for number_even in N_even:
        total += number_even
    for number_odd in N_odd:
        cal *= number_odd
    if cal == 1:
        cal = 0
    print(total, cal)




