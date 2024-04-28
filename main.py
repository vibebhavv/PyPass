import termcolor2
import colorama
from time import sleep, time
from colorama import Fore, init
import random
import string
import os

os.system('cls')

#Password generator
def passwd(length):
        alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        numsym = str("""1234567890"!@#$%^&*(){[]?|\-=:";'<>,.?}/""")
        combine = alpha+numsym
        last = ''.join(random.choice(combine) for i in range(length))
        print("\n┌──A strong password of", user_input, "character for you: ", Fore.GREEN + last)
        w = open("C:\Python 311\extpro\PassGen\All Passwords.txt", 'a')
        w.write("\n"+name+ " ==> " + last)
        w.close()
        return combine

#Autoreset colors
colorama.init(autoreset=True)

#Statements
print(Fore.YELLOW + "\nGreetings !")
print(Fore.YELLOW + "\nIts good to have a strong password. Let's make one for you -->")

#Main menu
x = "\n[1] Make password for you"
y = "\n[99] Exit"
print(Fore.CYAN + x, Fore.CYAN + y)
user_choice = input("\n[+] Choose from above: ")

while user_choice=='1':
    os.system("cls")
    passwd
    
#User choice of password length
    name = input("\nAssign a Name to your password to remember: ")
    user_input = int(input("Enter the length of password you want: "))
    passwd(user_input)
    
#Note
    print("└─>Your password is saved at ", Fore.GREEN + "(C:\Python 311\extpro\PassGen\All Passwords.txt)")
    print("")

    nxt = input("[+] Wan't to generate more passwords [Y/N]: ")

    if nxt=='Y' or nxt=='y':
        passwd

#Exit script
    elif nxt=='N' or nxt=='n':
        print(Fore.RED + "\nOperation Aborted by user !")
        break

    elif nxt!='N' or nxt!='n':
            print(Fore.RED + "\n Wrong Input!")
            break

if user_choice=='99':
        print(termcolor2.colored("\nGood Bye, Have a Nice Day :)", 'magenta'))
        exit
