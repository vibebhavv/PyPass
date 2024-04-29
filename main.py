import termcolor2
import colorama
from colorama import Fore
import random
import os
import platform 
import nacl.secret
import nacl.utils
import chardet

# branding about maker

# platform check
def plt_check_fun():      
    plt_check = platform.system()
    if plt_check.lower() == 'darwin':
        os.system('clear')
    elif plt_check.lower() == 'linux':
        os.system('clear')
    elif plt_check.lower() == 'windows':
         os.system('cls')

plt_check_fun()

# Password generator
def passwd(length):
        alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        numsym = r"""1234567890"!@#$%^&*(){[]?|\-=:";'<>,.?}/"""
        combine = alpha+numsym
        last = ''.join(random.choice(combine) for i in range(length))
        print("\n┌──A strong password of", user_input, "character for you:", Fore.GREEN + last)
        w = open(r"savedpass.txt", 'a')
        w.write("\n"+name+ " ---> " + last)
        w.close()
        return combine
    
# Password encrypter and decrypted
def encrypt_data():

    # Generate a random key
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    # Create a secret box with the key
    box = nacl.secret.SecretBox(key)

    # Function to encrypt a string
    def encrypt_string(string, box):
        return box.encrypt(string.encode()).ciphertext

    # Encrypt all strings in a file and overwrite the original file
    def encrypt_file(input_file, box):
        with open(input_file, 'rb') as f:
            plaintext = f.read()
            encrypted = box.encrypt(plaintext)
            
        with open(input_file, 'wb') as f:
            f.write(encrypted)
            
        # Save the key for decryption
        with open(input_file + ".key", 'wb') as f:
            f.write(key)

    # Encrypt the strings in the input file
    encrypt_file('savedpass.txt', box)


def decrypt_data():

    # Load the key from the file
    with open('savedpass.txt.key', 'rb') as f:
        key = f.read()

    # Create a secret box with the key
    box = nacl.secret.SecretBox(key)

    def decrypt_file(input_file, box):
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()

        print(Fore.YELLOW + "\nLoading all saved passwords...")

        # Split the encrypted data into individual strings
        encrypted_strings = encrypted_data.split(b'\n')

        for encrypted_string in encrypted_strings:
            if encrypted_string:
                decrypted = box.decrypt(encrypted_string)

                # Detect the encoding
                result = chardet.detect(decrypted)
                encoding = result['encoding']

                if encoding:
                    try:
                        decoded_string = decrypted.decode(encoding, errors='replace')
                        print("\n" + Fore.GREEN + decoded_string)
                    except UnicodeDecodeError:
                        print(Fore.RED + "\nError: Unable to decode the decrypted data.")
                else:
                    print(Fore.RED + "\nError: Unable to detect the encoding of the decrypted data.")

    # Decrypt the encrypted file and print the decrypted content
    decrypt_file('savedpass.txt', box)


#Autoreset colors
colorama.init(autoreset=True)

#Statements
print(Fore.YELLOW + "\nGreetings !")
print(Fore.YELLOW + "\nIts good to have a strong password. Let's make one for you ──>")

#Main menu
x = "\n[1] Make password for you"
y = "\n[2] View all passwords"
z = "\n[99] Exit"

print(Fore.CYAN + x, Fore.CYAN + y, Fore.CYAN + z)
user_choice = input("\n[+] Choose from above: ")

while user_choice=='1':
    plt_check_fun()
    passwd
    
#User choice of password length
    name = input("\n[*] Assign a Name to your password to remember: ")
    user_input = int(input("[+] Enter the length of password you want: "))
    passwd(user_input)
    
#Note
    print("└─>Your password is saved at:", Fore.GREEN + "savedpass.txt")
    encrypt_data()
    print("")

    nxt = input("[+] Wan't to generate more passwords [Y/N]: ")

    if nxt=='Y' or nxt=='y':
        passwd

#Exit script
    elif nxt=='N' or nxt=='n':
        print(Fore.RED + "\n[!] Operation Aborted by user !")
        break

    elif nxt!='N' or nxt!='n':
            print(Fore.RED + "\n[!] Wrong Input!")
            break

if user_choice=='2':
    plt_check_fun()
    decrypt_data()
    input("\nPress Enter to continue...")

if user_choice=='99':
        print(termcolor2.colored("\nGood Bye, Have a Nice Day :)", 'magenta'))
        exit
