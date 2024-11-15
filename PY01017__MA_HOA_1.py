for _ in range(int(input())):
    string = input()
    new_string = ""
    i = 0
    while i < len(string):
        count = 1
        while i < len(string)-1 and string[i] == string[i+1]:
            count += 1
            i += 1
        new_string = new_string + str(count) + string[i]
        i += 1
    print(new_string)
