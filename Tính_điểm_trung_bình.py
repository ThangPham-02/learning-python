N = int(input())
list_point = list(map(float, input().split()))
a = max(list_point)
b = min(list_point)
for x in range(list_point.count(a)):
    list_point.remove(a)
for y in range(list_point.count(b)):
    list_point.remove(b)
avg = 0
for i in list_point:
    avg += i
avg = avg / len(list_point)
print(round(avg, 2))
