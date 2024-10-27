so = int(input())
f = []
for i in range(0,so):
    f.append(int(input()))
output = []
for number in f:
    number_digits = [int(i) for i in str(number)]
    number_digits = list(enumerate(number_digits))
    mul = 1
    sum_odd = 0
    for index, item in number_digits:
        if index % 2 == 0:
            if item != 0:
                mul = mul * item
        else:
            sum_odd = sum_odd + item


