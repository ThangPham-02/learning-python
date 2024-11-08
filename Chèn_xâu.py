s1 = input()
s2 = input()
p = int(input())
new_string = s1[:p-1] + s2 + s1[p-1:]
print(new_string)