def tinh_giai_thua(a):
    cal = 1
    for i in range(2, a+1):
        cal *= i
    return cal

for _ in range(int(input())):
    N = input()
    total = 0
    for number in str(N):
        total += tinh_giai_thua(int(number))
    if total == int(N):
        print("Yes")
    else:
        print("No")
