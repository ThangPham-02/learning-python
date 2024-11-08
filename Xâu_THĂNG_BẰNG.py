# Trùng với bài khoảng cách ký tự
def khoang_cach(a1, a2):
    for i in range(1, len(a1)):
        if abs(ord(a1[i]) - ord(a1[i-1])) != abs(ord(a2[i]) - ord(a2[i-1])):
            return "NO"
    return "YES"

for x in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    print(khoang_cach(s1, s2))