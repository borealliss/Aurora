
flower= input("Input your choice's of flower :")
petal= int(input("Total of petals :"))
price= float(input("The price of the flower :"))

class Jualan:  
    
    def __init__(self, flower, petal, price):
        self.flower = flower
        self.petal =petal
        self.price =price

    def info(self):
        print(f"Bunga yang dipilih {self.flower}, Jumlah Petal {self.petal}, harganya {self.price}")

    def w(self, flower2):
        self.flower= flower2

    def e(self, petal2):
        self.petal=petal2

    def r(self, price2):
        self.price= price2

    def return1(self, flower2):
        return f"Bunga yang dipilih {self.flower}"

    def return2(self, petal2):
        return f"Jumlah Petal {self.petal}"

    def return3(self, price2):
        return f"harganya {self.price}"

jualan1= Jualan(flower, petal, price)
print(jualan1.info())

flower2= input("Input your choice's of flower :")
petal2= int(input("Total of petals :"))
price2= float(input("The price of the flower :"))
        
jualan2 = Jualan(flower2, petal2, price2)
print (jualan2.return1(flower2))
print (jualan2.return2(petal2))
print (jualan2.return3(price2))