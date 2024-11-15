st = str(input())
count_u = 0
count_l = 0
for i in st:
    if i.isupper():
        count_u += 1
    if i.islower():
        count_l += 1
if count_u > count_l :
    print(st.upper())
else:
    print(st.lower())
