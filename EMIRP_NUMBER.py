def check_nguyen_to(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for item in range(2, int(num ** 0.5)+1):
        if num % item == 0:
            return False
    return True

for _ in range(int(input())):
    number_N = int(input())
    output = []
    for number in range(1,int(number_N)):
        reversed_number = str(number)[::-1]
        if check_nguyen_to(number) and check_nguyen_to(int(reversed_number)):
            if str(number) != reversed_number and int(reversed_number) < number_N:
                if number not in output:
                    output.append(number)
                    output.append(int(reversed_number))
    for i in output:
        print(i, end = ' ')
    print('')


