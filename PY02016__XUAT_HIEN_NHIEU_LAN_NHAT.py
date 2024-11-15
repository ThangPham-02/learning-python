for i in range(int(input())):
    length = int(input())
    A =input().split()
    new_count ={}
    for number in A:
        if number not in new_count:
            new_count[number] = 1
        else:
            new_count[number] += 1
    def check(a, n):
        for x in a:
            if a[x] > n/2:
                return x
        return "NO"
    print(check(new_count, length))

