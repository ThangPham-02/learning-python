# N = input()
# N = N[::-1]
# count = 0
# new_N = ""
# for i in N:
#     if count == 3:
#         new_N += ","
#         count = 0
#     count += 1
#     new_N += i
# print(new_N[::-1])

N = int(input())
formatted_number = "{:,}".format(N)
print(formatted_number)