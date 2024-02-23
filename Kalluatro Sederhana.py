print("=======Kalkulator======")
print("Pilih Operasi yang akan digunakan")
Operasi=(float(input("ketik yang diinginkan 1=Kali,2=Bagi,3=Kurang,4=Tambah "))) 

Angka1=float(input("Masukkan Angka 1 = "))
Angka2=float(input("Masukkan Angka 2 = "))
 
if Operasi==1:
    print(Angka1*Angka2)
elif Operasi==2:
    print(Angka1/Angka2)
elif Operasi==3 :
    print(Angka1=Angka2)
elif Operasi==4 :
    print(Angka1+Angka2)
else :
    print('Anda salah memasukkan perintah')
