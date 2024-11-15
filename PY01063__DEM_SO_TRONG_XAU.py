#Cách 1: dùng đệ quy
# def counting(s,n,countt):
#     if n in s:
#         s = s[:s.index(n)] + s[s.index(n)+len(n):]
#         countt += 1
#         return counting(s,n,countt)
#     else:
#         return countt
#
# test = int(input())
# for i in range(test):
#     S = input()
#     N = input()
#     count = 0
#     print(counting(S,N,count))
# Cách 2: dùng hàm count()
for i in range(int(input())):
    s = input()
    n = input()
    print(s.count(n))


