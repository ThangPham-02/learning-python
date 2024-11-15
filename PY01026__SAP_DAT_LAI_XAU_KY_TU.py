def change_to_list(a, b):
    new_a = []
    new_b = []
    for i in a:
        new_a.append(i)
    for j in b:
        new_b.append(j)
    if sorted(new_a) == sorted(new_b):
        return "YES"
    else:
        return "NO"

test = int(input())
for x in range(1, test+1):
    s1 = input()
    s2 = input()
    print(f"Test {x}:", change_to_list(s1, s2))

