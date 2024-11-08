string_1 = input()
string_2 = input()
combine = []
for char_1 in string_1.lower().split():
    if char_1 not in combine:
        combine.append(char_1)
inter = []
for char_2 in string_2.lower().split():
    if char_2 not in combine:
        combine.append(char_2)
    if char_2 in string_1.lower().split() and char_2 not in inter:
        inter.append(char_2)
print(' '.join(sorted(combine)))
print(' '.join(sorted(inter)))
