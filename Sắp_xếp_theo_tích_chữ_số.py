def cal_(a):
    t = 1
    for i in a:
        t *= int(i)
    return t

test = int(input())
for _ in range(test):
    length = int(input())
    list_number = list(map(int, input().split()))
    result = {}
    for number in list_number:
        result[number] = cal_(str(number))
#sắp xếp theo tổng các chữ số của số (item[1]),
#nếu tổng bằng nhau thì sắp xếp theo giá trị của số (item[0])
#sắp xếp từ nhỏ đến lớn
    sorted_result = dict(sorted(result.items(), key = lambda item: (item[1], item[0])))
    for x in sorted_result:
        print(x, end = ' ')
    print('')