# class Person:
#     def __init__(self, name, age, gender, position):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.position = position
#
#     def move(self):
#         self.position = self.position + 100
#     def up(self):
#         self.position = self.position - 3
#     def down(self):
#         self.position = self.position - 1
#     def turn_left(self):
#         self.position = self.position + 5
#     def turn_right(self):
#         self.position = self.position + 10
# sonph = Person("SonPH", 20, "Nam", 0)
#
# print(sonph.name)
# print(sonph.age)
# print(sonph.gender)
# print(sonph.position)
# print("turn right:")
# sonph.turn_right()
# print(sonph.position)
# print("move:")
# sonph.move()
# print(sonph.position)
import decimal
from decimal import Decimal
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point2):
        tmp = ((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)
        distance = tmp.sqrt()
        return "{:.4f}".format(distance)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

