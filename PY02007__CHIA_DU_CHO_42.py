A = []
while len(A) < 10:
    A += list(map(int, input().split()))
new = []
for number in A:
    x = int(number) % 42
    if x not in new:
        new.append(x)
print(len(new))

