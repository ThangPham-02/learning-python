# so may man 2
so = int(input())
N = []
for i in range(so):
    N.append(int(input()))
count = 0
for i in N:
    for y in str(i):
       if y != "4" and y != "7":
           count += 1
    if count == 0:
        print("YES")
    else:
        print("NO")
    count = 0

