import main

welcome_messeg2 = "Selamat Datang di Warung Mini"

def start():
    style = "=" * (len(welcome_messeg2) + 8 )
    print(f"{style}")
    print(f"=== {welcome_messeg2} ===")
    print(f"{style}")

def makanan():
    messeg = "Menu Makanan"
    global totalmakanan
    global porsi
    style = "=" * (len(messeg) + 8 )
    print(f"{style}")
    print(f"=== {messeg} ===")
    print(f"{style}")

    print(f"1. Nasi Goreng Rp.13.000")
    print(f"2. Kentang Goreng Rp. 10.000")
    print(f"3. Sosis Bakar Rp. 8.000 ")

    nomor = int(input("Pilih Menu Makanan: "))
    porsi = int(input("Berapa Porsi: "))

    if nomor == 1:
        totalmakanan = porsi * 13_000
        print(f"{porsi}, Nasi Goreng = Rp. {totalmakanan}" )
    elif nomor == 2:
        totalmakanan = porsi * 10_000
        print(f"{porsi}, Kentang Goreng = Rp. {totalmakanan}" )
    elif nomor == 3:
        totalmakanan = porsi * 8_000
        print(f"{porsi}, Sosis Bakar = Rp. {totalmakanan}" )
    else:
        print("Pilihan Tidak Ada Di Menu, Silahkan Pilih Kemabli")
        makanan()

def minuman():
    messeg = "Menu Minuman"
    global totalminuman
    global gelas
    style = "=" * (len(messeg) + 8 )
    print(f"{style}")
    print(f"=== {messeg} ===")
    print(f"{style}")

    print(f"1. Es Teh Rp. 3.000")
    print(f"2. Jus Buah Rp. 5.000")

    nomor = int(input("Pilih Menu Minuman: "))
    gelas = int(input("Berapa Gelas: "))

    if nomor == 1:
        totalminuman = gelas * 3_000
        print(f"{porsi}, Es Teh = Rp. {totalminuman}" )
    elif nomor == 2:
        totalminuman = gelas * 5_000
        print(f"{gelas}, Jus Buah = Rp. {totalminuman}" )
    else:
        print("Pilihan Tidak Ada Di Menu, Silahkan Pilih Kembali")
        makanan()

def kasir():
    total = 0
    daftar_belanja = []

    while True:
        nama_menu = input("Masukkan nama barang (atau ketik 'selesai'): ")
        
        if nama_menu == "selesai":
            break
        
        try:
            harga = int(input(f"Masukkan harga untuk {nama_menu}: Rp "))
            total += harga
            daftar_belanja.append((nama_menu, harga))
        except ValueError:
            print("Masukkan angka yang valid untuk harga!")

    print(f"Total Harga: {total:.0f}")

    payment = int(input(f"Masukan Harga Yang Harus dibayarkan: "))
    money_buyer = int(input(f"Ketik Uang Yang Diberikan Pembeli: "))
    retur = money_buyer - payment

    print(f'Uang Kembalian Anda Adalah: {retur}')
    print(f'Silahkan Menunggu Pesanan Dimeja Anda')

    print("\n=== Struk Belanja ===")
    for menu, harga in daftar_belanja:
        print(f"{menu} - Rp {harga:.0f}")
    print(f"Total yang harus dibayar: Rp {total:.0f}")

    print(f'Harga Total = Rp. {total}')
    print(f'Uang Anda = Rp. {money_buyer}')
    print(f'Kemabalian Anda = {retur}')
    print(f'Terimasih Sudah Berbelanja Di Tempat Kami')


    choice8 = input(f"Apakah Anda Ingin Kembali Ke Menu Utama? [y/n]")
    if choice8 == "y":
        main.menu()
    elif choice8 == "n":
        makanan()
    else:
        exit()

if __name__ == "__main__":
    start()
    makanan()
    minuman()
    kasir() 