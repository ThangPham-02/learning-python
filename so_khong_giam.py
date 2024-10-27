len_number = int(input())
number = []
for unit1 in range(len_number):
    number.append(int(input()))
check = 0
for unit2 in number:
    numberlist = [int(i) for i in str(unit2)]
    decrease = numberlist[0]
    for unit4 in numberlist:
        if decrease > unit4:
            check += 1
            print(check)
if check == 0:
    print("YES")
else:
    print("NO")



#chưa được
