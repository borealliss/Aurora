print ("Key and Value Dictionary")
print("=============================================")
def rumus(data):
    for key,value in data.items():
        print (f"{key} : {value}")

dataanak = {}

tries = 0
while tries != 3:
    pertama = input("Masukkan key yang ingin ditambahkan :")
    kedua = input("Masukkan value yang ingin ditambahkan :")
    print("=============================================")
    dataanak[pertama]=kedua
    tries += 1
rumus(dataanak)
