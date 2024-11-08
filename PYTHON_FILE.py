name_file = input()
check = 0
if name_file[-3:].lower() == ".py":
    check += 1
for i in name_file:
    if i != '_' and i != '.' and not(i.isalpha()):
        check -= 1
if check == 1:
    print("yes")
else:
    print("no")
