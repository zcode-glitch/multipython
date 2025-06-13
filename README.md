# multi
In this repository, as a developer, I present one of the codes that I have created to make it easier for users so they don't get bored.
# In this code there is input that will produce output on the terminal, and the output is various things, for example: calculator, cashier, and games.
# For more information see: https://github.com/zcode-glitch/multipython.git

name: Multi Tools Python In Terminal

from libs import welcome_messeg, exit_program
from games import hamster
from tools import kalkulator, warung
from song import where_we_are_lyrics

def menu():
    user_option = int(input(f'''Menu Program:
    1. Find Hamster Game
    2. Kalkulator
    3. Warung
    4. Song
    5. Exit Program
    Silahkan Pilih: '''))

    if user_option == 1:
        hamster.start()
    elif user_option == 2:
        kalkulator.start()
    elif user_option == 3:
        warung.start()
        warung.makanan()
        warung.minuman()
        warung.kasir()
    elif user_option == 4:
        where_we_are_lyrics.running_lirik()
        where_we_are_lyrics.end()
    elif user_option == 5:
        exit_program()
        exit()
    else:
        print('Pilihan Tidak Tersedia !')
        menu()

def main():
    welcome_messeg()
    menu()

if __name__ == "__main__":
    main()
