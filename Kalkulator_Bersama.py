print ("Selamat Datang di Kalkulator Bersama")

tries=0
while tries != 3:
    Angkapertama = int(input("Silahkan ketik angka pertama:"))
    Angkakedua = int(input("Silahkan ketik angka kedua:"))
    print ("Mau diapain angkanya?")

    pilihan = input ("1(+) , 2(-), 3(*), 4(/):")

    if pilihan == "1":
        Hasil_tambah = (Angkapertama+Angkakedua)
        print (f"Hasil tambah dari {Angkapertama} dengan {Angkakedua} adalah {Hasil_tambah}")
    elif pilihan == "2":
        Hasil_kurang = (Angkapertama-Angkakedua)
        print  (f"Hasil kurang dari {Angkapertama} dengan {Angkakedua} adalah {Hasil_kurang}")
    elif pilihan == "3":
        Hasil_kali = (Angkapertama*Angkakedua)
        print (f"Hasil kali dari {Angkapertama} dengan {Angkakedua} adalah {Hasil_kali}")
    elif pilihan == "4":
        Hasil_bagi = (Angkapertama//Angkakedua)
        print  (f"Hasil bagi dari {Angkapertama} dengan {Angkakedua} adalah {Hasil_bagi}")
    tries += 1
    
