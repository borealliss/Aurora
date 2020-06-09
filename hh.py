pesanan1 = ["teh","kopi", "boba"]
for n in range(len(pesanan1)):
    print (n+1, pesanan1[n])

tambahan = input ("Ada tambahan ga?(y/n)")
while tambahan == "y":
        pesanan2 = input ("mau tambah apa lagi")
        tambahan = input ("Ada tambahan ga?(y/n)")
print ("saya ulang pesanannya ya")
for x in pesanan2:
    print (pesanan2)
