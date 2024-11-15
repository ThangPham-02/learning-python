for x in range(int(input())):
    number = int(input())
    number = str(number)
    #kiểm tra điều kiện 1
    check = 0
    if len(str(number)) % 2 != 0:
        check += 1
    # Kiểm tra điều kiện 2
    if str(number[0]) != str(number[1]):
        check += 1
    # kiểm tra điều kiện 3
    i = 0
    while i < len(str(number))-2:
        if str(number[i]) != str(number[i+2]):
            check -= 1
        i += 2
    if check == 2:
        print("YES")
    else:
        print("NO")



