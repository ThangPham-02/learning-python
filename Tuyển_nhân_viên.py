def check(a):
    if a > 9.5:
        return "XUAT SAC"
    if 9.5 > a >= 8:
        return "DAT"
    if 8 > a >= 5:
        return "CAN NHAC"
    else:
        return "TRUOT"

test = int(input())
dic = {}
for i in range(1, test + 1):
    name = input()
    theory_point = input()
    practice_point = input()
    theory_point = str(float(theory_point))
    practice_point = str(float(practice_point))
    if len(theory_point) == 2:
        theory_point = theory_point[0] + "." + theory_point[-1]
    if len(practice_point) == 2:
        practice_point = practice_point[0] + "." + practice_point[-1]
    average_point = (float(theory_point) + float(practice_point)) / 2
    dic["TS0" + str(i) + " " + name] = round(average_point, 2)
sorted_dic = dict(sorted(dic.items(), key = lambda item: item[1], reverse= True))
for x in sorted_dic:
    print(x, f"{sorted_dic[x]:.2f}", check(sorted_dic[x]))

# WA








