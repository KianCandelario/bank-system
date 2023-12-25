#from colorama import Fore
import os
import time

# Variables
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

def menu_error_notifier1():
    print("You can only choose [1], [2], or [0]. Please try again.")
    time.sleep(3)  # 3 second delay before clearing the screen
    clear()

def menu_error_notifier2():
    print("You entered an invalid input. Please try again.")
    time.sleep(3)  # 3 second delay before clearing the screen
    clear()




# Main functions
def initialMenu():
    while True:
        try:
            valid_choices = [0,1,2]

            menu_layout(title="KiBank Illuminaire", choice1="Open an Account", choice2="Client Management", choice3="Exit")
            initial_menu_choice = int(input("\tEnter your choice: "))

            print()

            if initial_menu_choice not in valid_choices:
                menu_error_notifier1()
                continue
            else:
                return initial_menu_choice
        except:
            menu_error_notifier2()
            continue


def clientManagement():
    while True:
        try:
            valid_choices = [0,1,2]

            menu_layout(title="Client Management", choice1="List All Clients", choice2="Find a Client", choice3="Back")

            client_m_choice = int(input("\tEnter your choice: "))

            print()

            if client_m_choice not in valid_choices:
                menu_error_notifier1()
                continue
            else:
                return client_m_choice
        except:
            menu_error_notifier2()
            continue


def openAccount():
    while True:
        try:
            valid_choices = [0,1,2]

            menu_layout(title="KiBank Illuminaire", choice1="New Client", choice2="Old Client", choice3="Back")
            
            open_acc_choice = int(input("\tEnter your choice: "))

            print()

            if open_acc_choice not in valid_choices:
                menu_error_notifier1()
                continue
            else:
                return open_acc_choice
        except:
            menu_error_notifier2()
            continue




create_acc_or_client = initialMenu()

if create_acc_or_client == 1:
    open_acc_or_client_m = openAccount()
elif create_acc_or_client == 2:
    open_acc_or_client_m = clientManagement()
elif create_acc_or_client == 0:
    exit()