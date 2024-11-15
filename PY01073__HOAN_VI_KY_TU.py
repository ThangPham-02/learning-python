from itertools import permutations

string = input()
result = permutations(string)
for i in result:
    print(''.join(i))

