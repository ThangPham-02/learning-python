for _ in range(int(input())):
    no_decrease_number = input()
    check = 1
    for i in range(len(no_decrease_number)-1):
        if no_decrease_number[i] > no_decrease_number[i+1]:
            check += 1
    if check == 1:
        print("YES")
    else:
        print("NO")

