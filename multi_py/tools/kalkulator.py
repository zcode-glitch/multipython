import main
import socket

pc_name2 = socket.gethostname()

def start():

    while True:
        # Pesan Pembuka
        print(f"Hallo {pc_name2} , selamat datang di kalkulator!")

        # Minta dua angka dari pengguna
        angka1 = input("Masukkan angka pertama: ")
        angka2 = input("Masukkan angka kedua: ")

        # Ubah dari teks (string) ke angka (integer)
        angka1 = int(angka1)
        angka2 = int(angka2)

        # Hitung hasil penjumlahan
        hasil = angka1 + angka2

        # Tampilkan hasilnya
        print(f"Hasil dari {angka1} + {angka2} adalah {hasil}")

        choice = input("Ingin Kembali ke Menu Utama? (y/n) ")
        if choice == "y":
            main.menu()
        elif choice == "n":
            continue
        else:
            exit()

if __name__ == "__main__":
    start()