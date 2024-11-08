for _ in range(int(input())):
    S = input()
    total = 0
    string = []
    for i in S:
        if i.isdigit():
            total += int(i)
        if i.isalpha():
            string.append(i)
    result = ''
    for x in sorted(string):
        result += x
    print(result + str(total))
