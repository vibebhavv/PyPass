'''
Project: PyPass (Python based password generator and manager)
Author: https://github.com/G0dVai
[ DONT CHANGE ANY THING IF YOU DONT KNOW ANTHING ABOUT PROGRAMMING OR ELSE IT WILL AFFECT ENCRYPTIONA AND DECRYPTION !!! ]
'''

import colorama
from colorama import Fore
import random
import os
import platform 
import nacl.secret
import nacl.utils

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

# branding about maker
print(Fore.GREEN + "\n╔═╗┬ ┬╔═╗┌─┐┌─┐┌─┐")
print(Fore.GREEN + "╠═╝└┬┘╠═╝├─┤└─┐└─┐")
print(Fore.GREEN + "╩   ┴ ╩  ┴ ┴└─┘└─┘")
print("\nDeveloped by: https://github.com/vibebhavv")
print("[ A simple Password generator and manager. ]")

# Password generator
def passwd(length):
    alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    numsym = r"""1234567890"!@#$%^&*(){[]?|\-=:";'<>,.?}/"""
    combine = alpha+numsym
    last = ''.join(random.choice(combine) for i in range(length))
    print("\n┌──A strong password of", length, "characters for you:", Fore.GREEN + last)
    return last

def encrypt_data(data, key):
    # Create a secret box with the key
    box = nacl.secret.SecretBox(key)
    
    # Encrypt the data
    encrypted_data = box.encrypt(data.encode())
    
    return encrypted_data

def decrypt_data(encrypted_data, key):
    # Create a secret box with the key
    box = nacl.secret.SecretBox(key)
    
    # Decrypt the data
    decrypted_data = box.decrypt(encrypted_data).decode()
    
    return decrypted_data

#Autoreset colors
colorama.init(autoreset=True)

#Statements
print(Fore.YELLOW + "\nGreetings !")
print(Fore.YELLOW + "\nIt's good to have a strong password. Let's make one for you ──>")

#Main menu
x = "\n[1] Make password for you"
y = "\n[2] View all passwords"
z = "\n[99] Exit"

print(Fore.CYAN + x, Fore.CYAN + y, Fore.CYAN + z)
user_choice = input("\n[+] Choose from above: ")

key_path = "encpasskey.key"

# Check if key file exists, if not generate and save the key
if not os.path.exists(key_path):
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
else:
    # Load the key from file
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

while True:
    if user_choice == '1':
        plt_check_fun()
        # User choice of password length
        name = input("\n[*] Assign a Name to your password to remember: ")
        user_input = int(input("[+] Enter the length of password you want: "))
        password = passwd(user_input)
        
        # Encrypt the password and save it
        encrypted_password = encrypt_data(password, key)
        
        with open("savedpass.txt", 'a') as f:
            f.write(name + " ---> " + encrypted_password.hex() + "\n")
        
        print("└─>Your password is saved at:", Fore.GREEN + "savedpass.txt")
        
        nxt = input("\n[+] Want to generate more passwords [Y/N]: ")
        
        if nxt.lower() != 'y':
            print(Fore.RED + "\n[!] Operation Aborted by user !")
            break
    
    elif user_choice == '2':
        plt_check_fun()
        print(Fore.YELLOW + "[>] Loading all saved passwords...\n") 
        
        with open("savedpass.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(" ---> ")
                if len(parts) == 2:
                    name, encrypted_password_hex = parts
                    encrypted_password = bytes.fromhex(encrypted_password_hex.strip())
                    decrypted_password = decrypt_data(encrypted_password, key)
                    print(name.strip(), "--->", decrypted_password)
        
        input("\nPress Enter to continue...")
        break
    
    elif user_choice == '99':
        print(Fore.MAGENTA + "\nGoodbye, Have a Nice Day :)")
        break
    
    else:
        print(Fore.RED + "\n[!] Invalid choice. Please choose again.")
        user_choice = input("\n[+] Choose from above: ")

