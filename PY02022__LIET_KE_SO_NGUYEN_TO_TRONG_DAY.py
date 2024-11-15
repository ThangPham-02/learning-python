def so_nguyen_to(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for item in range(2, int(num ** 0.5)+1):
        if num % item == 0:
            return False
    return True

N = int(input())
list_number = list(map(int, input().split()))
result = []
for number in list_number:
    if so_nguyen_to(number) and number not in result:
        result.append(number)
        print(number, list_number.count(number))
