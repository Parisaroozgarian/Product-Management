class product:
    def __init__(self,id,name,type,price):
        self.id=id
        self.name=name
        self.type=type
        self.price=price

    def show(self):
        print('Name of Product: '+self.name)
        print('Type of Product: '+self.type)
        print('Price: '+str(self.price))

    def getprice(self):
        return self.price

class product2(product):
    def __init__(self,rank,id,name,type,price):
        product.__init__(self,id,name,type,price)
        self.rank=rank

    def show(self):
        product.show(self)
        print('Rank: '+str(self.rank))

p2=product2(4,2,'Apple','Iphone',2000)
p2.show()