peserta ={}
ikut =[]

while True:
    peserta ={}
    nama = input ("Siapakah nama anda :")
    umur = input ("Berapakah umur anda :")
    lomba = input ("Jenis lomba yang diikuti :")

    peserta["nama:"]=nama
    peserta["umur:"]=umur
    peserta["lomba:"]=lomba

    tambahan = input ("Ada tambahan ga?(y/n)")
    ikut.append(peserta)

    if tambahan =="y":
        continue
    else:
        break

    print ("saya ulang peserta")
for y in ikut:
    for key,value in y.items():
        print(key,value)