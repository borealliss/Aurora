username = "Gisela"
Password = "Aurora"

tries= 0

while tries != 3:
    Nama_User = input("Username:")
    Kata_Sandi = input("Password:") 
     
    if Nama_User == username and Kata_Sandi == Password:
        print ("Berhasil")
        break 
    print ("Coba lagi")
        