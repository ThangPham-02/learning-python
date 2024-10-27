def change(x):
    if x >= 39:
        return 9.0
    elif x >= 37:
        return 8.5
    elif x >= 35:
        return 8.0
    elif x >= 33:
        return 7.5
    elif x >= 30:
        return 7.0
    elif x >= 27:
        return 6.5
    elif x >= 23:
        return 6.0
    elif x >= 20:
        return 5.5
    elif x >= 16:
        return 5.0
    elif x >= 13:
        return 4.5
    elif x >= 10:
        return 4.0
    elif x >= 7:
        return 3.5
    elif x >= 5:
        return 3.0
    else:
        return 2.5
length = int(input())
N = []
for i in range(length):
    N = list(map(float, input().split()))
    listening = N[0]
    reading = N[1]
    speaking = N[2]
    writing = N[3]
    point = (change(listening) + change(reading) + speaking + writing)/4
    if point - int(point) >= 0.75:
        print(int(point) + 1)
    elif point - int(point) >= 0.25:
        print(int(point) + 0.5)
    else:
        print(int(point) + 0.0)



