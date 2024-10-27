#
# t = int(input())
# outputt = []
# while t > 0:
#     a, b = input().split()
#     day = int(a)
#     month = int(b)
#     if month == 1:
#         if day <= 19:
#             outputt.append("Ma Ket")
#         else:
#             outputt.append("Bao Binh")
#     elif month == 2:
#         if day <= 18:
#             outputt.append("Bao Binh")
#         else:
#             outputt.append("Song Ngu")
#     elif month == 3:
#         if day <= 20:
#             outputt.append("Song Ngu")
#         else:
#             outputt.append("Bach Duong")
#     elif month == 4:
#         if day <= 19:
#             outputt.append("Bach Duong")
#         else:
#             outputt.append("Kim Nguu")
#     elif month == 5:
#         if day <= 20:
#             outputt.append("Kim Nguu")
#         else:
#             outputt.append("Song Tu")
#     elif month == 6:
#         if day <= 22:
#             outputt.append("Song Tu")
#         else:
#             outputt.append("Cu Giai")
#     elif month == 7:
#         if day <= 22:
#             outputt.append("Cu Giai")
#         else:
#             outputt.append("Su Tu")
#     elif month == 8:
#         if day <= 22:
#             outputt.append("Su Tu")
#         else:
#             outputt.append("Xu Nu")
#     elif month == 9:
#         if day <= 22:
#             outputt.append("Xu Nu")
#         else:
#             outputt.append("Thien Binh")
#     elif month == 10:
#         if day <= 22:
#             outputt.append("Thien Binh")
#         else:
#             outputt.append("Thien Yet")
#     elif month == 11:
#         if day <= 22:
#             outputt.append("Thien Yet")
#         else:
#             outputt.append("Nhan Ma")
#     else:
#         if day <= 21:
#             outputt.append("Nhan Ma")
#         else:
#             outputt.append("Ma Ket")
#     t -= 1
# for i in outputt:
#     print(i)
t = int(input())

while t > 0:
    [a, b] = input().split()
    d = int(a)
    m = int(b)
    if m == 1:
        if d < 20:
            print("Ma Ket")
        else:
            print("Bao Binh")
    elif m == 2:
        if d < 19:
            print("Bao Binh")
        else:
            print("Song Ngu")
    elif m== 3:
        if d < 21:
            print("Song Ngu")
        else:
            print("Bach Duong")
    elif m == 4:
        if d < 20:
            print("Bach Duong")
        else:
            print("Kim Nguu")
    elif m == 5:
        if d < 21:
            print("Kim Nguu")
        else:
            print("Song Tu")
    elif m == 6:
        if d < 21:
            print("Song Tu")
        else:
            print("Cu Giai")
    elif m == 7:
        if d < 23:
            print("Cu Giai")
        else:
            print("Su Tu")
    elif m == 8:
        if d < 23:
            print("Su Tu")
        else:
            print("Xu Nu")
    elif m == 9:
        if d < 23:
            print("Xu Nu")
        else:
            print("Thien Binh")
    elif m == 10:
        if d < 23:
            print("Thien Binh")
        else:
            print("Thien Yet")
    elif m == 11:
        if d < 23:
            print("Thien Yet")
        else:
            print("Nhan Ma")
    else:
        if d < 22:
            print("Nhan Ma")
        else:
            print("Ma Ket")
    t -= 1

