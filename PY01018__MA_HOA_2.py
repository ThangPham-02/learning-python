while 1:
    S = input()
    if S[0] == "0":
        break
    K, S = S.split()
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    res = ''
    for i in S:
        res += P[(P.index(i)+int(K)) % 28]
    print(res[::-1])


