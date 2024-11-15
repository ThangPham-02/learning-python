test = int(input())
for _ in range(test):
    string = input()
    new = ''
    res = []
    for i in range(len(string)-1):
        if string[i].isdigit():
            new = new + string[i]
            if string[i+1].isalpha():
                res.append(int(new))
                new = ''
        if i == len(string)-2 and string[i+1].isdigit():
            new = new + string[i+1]
            res.append(int(new))
    print(min(res))