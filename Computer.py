class Computer:

    def __init__(self, __maxprice):
        self.__maxprice = __maxprice

    def sell(self):
        print("Giá bán sản phẩm là: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer(900)
c.sell()

# thay đổi giá:
c.__maxprice = 1000
c.sell()

# sử dụng hàm để thay đổi giá:
c.setMaxPrice(1000)
c.sell()