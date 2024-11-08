def check(n):
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return False
    return True
for _ in range(int(input())):
    beautiful_number = input()
    list_number = []
    for number in beautiful_number:
        if number not in list_number:
            list_number.append(number)
    if len(list_number) == 2 and check(beautiful_number):
        print("YES")
    else:
        print("NO")



