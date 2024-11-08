for _ in range(int(input())):
    n = int(input())
    list_number = list(map(int, input().split()))
    count = 0
    for number in range(min(list_number) + 1, max(list_number)):
        if number not in list_number:
            count += 1
    print(count)

