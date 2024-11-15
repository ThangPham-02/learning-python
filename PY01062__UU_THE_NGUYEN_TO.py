# Trùng với bài chữ số nguyên tố
def check_nguyen_to(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for item in range(2, int(number ** 0.5)+1):
        if number % item == 0:
            return False
    return True

for ok in range(int(input())):
    number_N = int(input())
    count_nguyen_to = 0
    count_not = 0
    for i in str(number_N):
        if check_nguyen_to(int(i)):
            count_nguyen_to += 1
        else:
            count_not += 1
    if check_nguyen_to(len(str(number_N))) and count_nguyen_to > count_not:
        print("YES")
    else:
        print("NO")