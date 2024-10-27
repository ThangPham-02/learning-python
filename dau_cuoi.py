# dau cuoi
so = int(input())
f = []
for i in range(0,so):
    f.append(int(input()))
for number in f:
    end = number % 100
    first = number // (10**(len(str(number))-2))
    if end == first :
        print("YES")
    else:
        print("NO")





