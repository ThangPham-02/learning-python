for _ in range(int(input())):
    list_ = list(map(int, input().split()))
    x1, y1 = list_[0], list_[1]
    x2, y2 = list_[2], list_[3]
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    print("{:.4f}".format(distance))