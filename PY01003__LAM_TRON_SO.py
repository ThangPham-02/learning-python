
# a = number
def round_number(a, count):
    divisor = 10 ** count
    rounded_number = a
    if a % divisor >= 5 * (10 ** (count-1)):
        rounded_number = (a // divisor) * divisor + divisor
    if a % divisor < 5 * (10 ** (count-1)):
        rounded_number = (a // divisor) * divisor
    return rounded_number

# b = number
def rounder(b, count = 0):
    if b <= 10:
        return b
    count += 1
    if count == len(str(b)):
        return b
    return rounder(round_number(b, count), count)

test = int(input())
for i in range(test):
    number = int(input())
    print(rounder(number))