for _ in range(int(input())):
    number = int(input())
    i = 2
    result = '1 * '
    while number > 1:
        count = 0
        while number % i == 0:
            count += 1
            number //= i
        if count > 0:
            result += str(i) + '^' + str(count) + ' * '
        i += 1
    print(result[:-3])

