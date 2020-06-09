anak = {}

nama = input("Masukkan nama anda:")
umur = int(input("Masukkan umur anda:"))
tinggi = int(input("Masukkan tinggi anda:"))
alamat = input("Masukkan alamat anda:")

anak["nama"] = nama
anak["umur"] = umur
anak["tinggi"] = tinggi
anak["alamat"] = alamat

for key,value in anak.items():
    print (f'saya adalah {nama} umur saya adalah {umur}')