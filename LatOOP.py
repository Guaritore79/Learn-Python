import os

os.system("cls")
class RekeningBank:
    def __init__(self, nama, saldo, norek, password):
        self.nama = nama
        self.saldo = saldo
        self.norek = norek
        self.password = password

    def cetak_saldo(self):
        os.system("cls")
        print(f"Nama : {self.nama}")
        print(f"Saldo anda : {self.saldo}")
    
    def menabung(self, jumlah):
        self.saldo += jumlah
        return self.saldo
    
    def tarik(self, penarikan):
        if penarikan > self.saldo:
            print(f"Tidak dapat melakukan penarikan, saldo anda hanya {self.saldo}")
        else:
            self.saldo -= penarikan
            return self.saldo
    def info (self):
        os.system("cls")
        print(f"Nama : {self.nama}")
        print(f"No Rekening : {self.norek}")
        print(f"Saldo : {self.saldo}")

def menu (nasabah):
    while True:
        os.system('cls')
        print("=== Bank ===")
        print(f"Selamat datang {nasabah.nama}")
        print("\nSilahkan pilih menu")
        print("1. Cek Saldo")
        print("2. Menabung")
        print("3. Tarik Uang")
        print("4. Informasi akun")
        pilihan = int(input("Pilihan : "))

        if pilihan == 1 :
            nasabah.cetak_saldo()
            os.system("pause")
        elif pilihan == 2:
            jumlah = int(input("Masukkan jumlah yang ingin ditabungkan : "))
            nasabah.menabung(jumlah)
            print("menabung berhasil dilkakukan")
            os.system("pause")
        elif pilihan == 3:
            jumlah = int(input("Masukkan jumlah yang ingin ditarik : "))
            nasabah.tarik(jumlah)
            os.system("pause")
        elif pilihan == 4:
            nasabah.info()
            os.system("pause")
        else:
            print("Masukkan pilihan dengan benar")
            os.system("pause")

def registrasi ():
    os.system('cls')
    print("=== Registrasi ===")
    nama = input("Masukkan nama : ")
    saldo = int(input("Masukkan saldo awal : "))
    norek = input("Masukkan no rekening : ")
    password = input("Masukkan password anda : ")

    nasabah = RekeningBank(nama, saldo, norek, password)
    return nasabah

def login(nasabah):
    while True:
        os.system('cls')
        print("=== Login ===")
        username = input("Masukkan nama anda : ")
        password = input("Masukkan password anda : ")

        if username == nasabah.nama and password == nasabah.password:
            print("Login berhasil")
            os.system("pause")
            menu(nasabah)
        else:
            print("Login gagal")
            os.system("pause")


def opsi_menu():
    nasabah = None
    while True:
        os.system('cls')
        print("1. Registrasi")
        print("2. Login")
        pilihan = int(input("Pilihan : "))
        
        if pilihan == 1:
            nasabah = registrasi()
            os.system('pause')
        elif pilihan == 2:
            if nasabah:
                login(nasabah)
            else:
                print("Silahkan registrasi terlebih dahulu")
                os.system("pause")

        else:
            print("Pilihan tidak valid")
            os.system("pause")
        

opsi_menu()

