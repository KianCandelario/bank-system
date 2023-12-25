#from colorama import Fore
import os
import time

# Variables
INITIAL_MENUS_VALID_CHOICES = [0,1,2]
create_acc_or_client = 0
open_acc_or_client_m = 0




# Auxillary functions
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu_layout(title, choice1, choice2, choice3):
    print("====================================")
    print(f"\t{title}")
    print("====================================")

    print()

    print(f"\t[1] {choice1}")
    print(f"\t[2] {choice2}")
    print(f"\t[0] {choice3}")

    print()

    print("====================================")

def menu_notifier(message):
    print(message)
    time.sleep(3)  # 3 second delay before clearing the screen
    clear()




# Main functions
def initialMenu():
    while True:
        try:
            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="KiBank Illuminaire", choice1="Open an Account", choice2="Client Management", choice3="Exit")
            initial_menu_choice = int(input("\tEnter your choice: "))

            print()

            if initial_menu_choice not in valid_choices:
                print()
                menu_notifier(message="You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return initial_menu_choice
        except:
            print()
            menu_notifier(message="You entered an invalid input. Please try again.")
            continue


def clientManagement():
    while True:
        try:
            print("====================================")
            print()
            menu_notifier(message="You selected [2] Client Management. Please wait a second...")

            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="Client Management", choice1="List All Clients", choice2="Find a Client", choice3="Back")

            client_m_choice = int(input("\tEnter your choice: "))

            if client_m_choice not in valid_choices:
                print()
                menu_notifier(message="You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return client_m_choice
        except:
            print()
            menu_notifier(message="You entered an invalid input. Please try again.")
            continue


def openAccount():
    while True:
        try:
            print("====================================")
            print()
            menu_notifier(message="You selected [1] Open an Account. Please wait a second...")

            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="KiBank Illuminaire", choice1="New Client", choice2="Old Client", choice3="Back")
            
            open_acc_choice = int(input("\tEnter your choice: "))


            if open_acc_choice not in valid_choices:
                print()
                menu_notifier(message="You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return open_acc_choice
        except:
            print()
            menu_notifier(message="You entered an invalid input. Please try again.")
            continue




create_acc_or_client = initialMenu()

if create_acc_or_client == 1:
    open_acc_or_client_m = openAccount()
elif create_acc_or_client == 2:
    open_acc_or_client_m = clientManagement()
elif create_acc_or_client == 0:
    print("Thank you. Please come again!")
    print()
    exit()