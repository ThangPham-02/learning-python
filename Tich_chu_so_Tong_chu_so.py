test = int(input())
for i in range(test):
    n = int(input())
    N = []
    for x in str(n):
        N.append(int(x))
    N_even = []
    N_odd = []
    for item in range(len(N)):
        if item % 2 == 0 and N[item] != 0:
            N_even.append(N[item])
        else:
            N_odd.append(N[item])
    total = 0
    cal = 1
    for number_even in N_even:
        cal *= number_even
    for number_odd in N_odd:
        total += number_odd
    print(cal, total)


