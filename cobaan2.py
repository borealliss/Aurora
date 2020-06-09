
bahan1: input("Masukkan bahan pertama :")
bahan2: input("Masukkan bahan kedua :")
bahan3: input("Masukkan bahan ketiga :")
alat: input("Masukkan alat yang digunakan :")
hasil: input("Hasil yang didapat :")
class Masak:    
    def __init__(self, bahan1, bahan2, bahan3, alat, hasil ):
        self.bahan1: bahan1
        self.bahan2: bahan2
        self.bahan3: bahan3
        self.alat: alat
        self.hasil: hasil

    def info(self):
        print(f"Campurkan{self.bahan1} dengan {self.bahan2} dan {self.bahan3} aduk. Kemudian masak di {self.alat} akan menghasilkan {self.hasil}")
masak1= Masak(bahan1, bahan2, bahan3, alat, hasil)

masak1.info()