import random
import main 
import socket 

pc_name3 = socket.gethostname()

def start():

    while True:

        print(f'{pc_name3} Welcome In Find Hamster Python Game')

        result = random.randint (1, 5)

        hole = "|_|"
        hole2= [hole] * 5

        tmp_hole2 = hole2.copy ()
        hole2[result - 1] = "|0.0|" 

        tmp_hole2 = ' '.join(tmp_hole2)
        hole2 = ' '.join(hole2)
    
        print(f'''
        Kami Telah Meyiapkan Goa Untuk Anda Mencari Hamster Pada Game ini
            
        {tmp_hole2}   
        ''')

        pilihan_user = int(input("Menurut Anda Di Goa Nomor Berapakah Hamster Itu Berada: 1/ 2/ 3/ 4/ 5? "))

        while pilihan_user >  5 :
                pilihan_user = int(input("Angkanya Cuman Sampe 5, Ketik Ulang: "))

        if pilihan_user == result:
            print(f'''{hole2}
            Selamat Anda Menang Karena Hamster Berada di Goa Nomor {result} dan Anda Menjawab {pilihan_user}
            ''')
        else:
            print(f'''
            {hole2}

            Maaf Anda Kalah!, Karena Jawaban Anda Adalah {pilihan_user} Sedangkan Hamster Berada di Goa {result}
            ''')

        play_again = input("Apakah Anda Ingin Mengulangi Game Ini? (y/n)")

        if play_again == "n":
             main.menu()
        elif play_again == "y": 
            continue
        else:
            print('Program Akan di Hentikan !!')
            break

if __name__ == "__main__":
     start()