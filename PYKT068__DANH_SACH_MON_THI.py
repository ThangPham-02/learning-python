dic = []
for _ in range(int(input())):
    ma_mon = input()
    ten_mon = input()
    hinh_thuc = input()
    dic.append(ma_mon + ' ' + ten_mon + ' ' + hinh_thuc)

sorted_dic = sorted(dic)
for i in sorted_dic:
    print(f"{i}")