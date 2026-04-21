class Laptop:
    def __init__(self):
        self.__maxprice = 1000
     
    def sell(self):
        print("Selling price : {}", format(self.__maxprice))

    def SetMaxPrice(self, price):
        self.__maxprice = price

l = Laptop()
l.sell()

# change the price 
l.__maxprice = 2000
l.sell()

# using setter function
l.SetMaxPrice(2000)
l.sell()