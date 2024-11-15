def counting(a, count):
    reversed_a = a[::-1]
    if int(a) % 7 == 0:
        return int(a)
    total = int(a) + int(reversed_a)
    count += 1
    if total % 7 == 0:
        return total
    if count == 1000:
        return -1
    return counting(str(total), count)

for _ in range(int(input())):
    number = input()
    step = 0
    print(counting(number, step))
