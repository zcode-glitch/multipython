import socket
from time import sleep

pc_name = socket.gethostname()

def welcome_messeg():
    style = "=" * (len(pc_name) + 14 )
    print(f"{style}")
    print(f"=== Hallo {pc_name} ===")
    print(f"{style}")

def exit_program():
    print('Program Akan di Hentikan !!')
    sleep(1)
    print('3...')
    sleep(1)
    print('2..')
    sleep(1)
    print('1.')
    print('program dihentikan!!')

if __name__ == "__main__":
    welcome_messeg()
    exit_program()