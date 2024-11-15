def price(a):
    if a == "5":
        return 10000
    elif a == "7":
        return 15000
    elif a == "2":
        return 20000
    elif a == "29":
        return 50000
    else:
        return 70000
dic = {}
for i in range(int(input())):
    _list = input().split()
    if _list[-2] == "OUT":
        continue
    if dic.get(_list[-1]) is None:
        dic[_list[-1]] = price(_list[-3])
    else:
        dic[_list[-1]] += price(_list[-3])
for x in sorted(dic):
    print(f"{x}: {dic[x]}")


