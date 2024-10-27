# chia het cho 3
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
total = 0
for a in l:
    for b in str(a):
        total += int(b)
    if  total % 3 == 0:
        print("YES")
        total = 0
    else:
        print("NO")
        total = 0
