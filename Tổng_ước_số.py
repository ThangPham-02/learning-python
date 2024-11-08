test = int(input())
list_number = []
for _ in range(test):
    list_number.append(int(input()))
total = 0
for number in list_number:
    i = 2
    while number != 1:
        if number % i == 0:
            total += i
            number = number / i
        else:
            i += 1
print(total)

# TLE

