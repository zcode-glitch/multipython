import main 
import sys
import time 

def running_lirik():
    lyrics = [
        ("Summer days rushin' by you and me", 0.1),
        ("Makes it harder to see underneath", 0.1),
        ("Did we ever know? Did we ever know?", 0.1),
        ("Did we ever know? (Did we ever know?)", 0.1),

        ("Is it all inside of my head?", 0.1),
        ("Maybe you still think I don't care", 0.1),
        ("But all I need is you", 0.1),
        ("Yeah, you know it's true, yeah, you know it's true", 0.1),

        ("Forget about where we are and let go", 0.1),
        ("We're so close", 0.1),
        ("If you don't know where to start, just hold on", 0.1),
        ("And don't run, no", 0.1),
        ("We're looking back, we messed around", 0.1),
        ("But that was then and this is now", 0.1),
        ("All we need's enough love to hold us", 0.1),
        ("Where we are", 0.1),
    ]

    delay = [0.3, 0.1, 0.1, 0.1, 0.4, 0.1, 0.1, 0.1, 0.3, 0.3, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1]
    print("== Where We Are - One Direction ==")
    time.sleep(2)
    for i, (line_song, delay_character) in enumerate(lyrics):
        for character in line_song:
            print(character, end='')
            sys.stdout.flush()
            time.sleep(delay_character)
        time.sleep(delay[i])
        print('')
    print("// Code By ZxCode")

def end():
    choice10 = input("Apakah Ingin Kembali Ke Menu Utama? [y/n]")
    if choice10 == "y":
        main.menu()
    elif choice10 == "n":
        running_lirik


if __name__ == "__main__":
    running_lirik()
    end()