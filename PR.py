print ("Kapan Tanggal Ulang Tahun Spongebob?")

tries = 0
while tries != 3:
    tanggal = int(input("Masukkan tanggal tebakan:"))
    if tanggal < 17:
        print ("Terlalu awal")
    elif 32>tanggal > 17:
        print ("Sudah lewat")
    elif tanggal == 17:
        print ("Penggemar sejati ^_^")
        break
    else:
        print ("1 Bulan maksimal 31 hari >_<")
tries +=1
        
    
