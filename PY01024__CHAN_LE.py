for i in range(int(input())):
    N = input()
    total = 0
    for number in N:
        total += int(number)
    check = 0
    item = 0
    while item < len(N)-1:
        if abs(int(N[item]) - int(N[item+1])) == 2 :
            check += 1
        item += 1
    if check != 0 and total % 10 == 0:
        print("YES")
    else:
        print("NO")




