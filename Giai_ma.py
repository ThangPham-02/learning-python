for _ in range(int(input())):
    string = input()
    new_string = ''
    for i in range(len(string)):
        if string[i].isdigit():
            x = int(string[i])
            new_string = new_string + string[i-1]*int(string[i])
    print(new_string)
