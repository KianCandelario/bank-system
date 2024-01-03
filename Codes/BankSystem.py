import os
import sys
import time
from BankAccount import BankAccount
from BankClient import BankClient

##### Class instance
CLIENT_INSTANCE = BankClient()
ACCOUNT_INSTANCE = BankAccount()

##### Global Variables
INITIAL_MENUS_VALID_CHOICES = [0,1,2]
create_acc_or_client = 0
open_acc_or_client_m = 0

ba_cursor = BankAccount.CURSOR
ba_configs = BankAccount.ACCOUNT_CONFIG
ba_db = BankAccount.DATABASE

bc_cursor = BankClient.CURSOR
bc_configs =  BankClient.CLIENT_CONFIG
bc_db = BankClient.DATABASE



###### Auxillary functions
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
    time.sleep(5)  # 5 second delay before clearing the screen
    clear()

def get_clientID_by_PIN(pin):
    query = f"SELECT {bc_configs['column1']} FROM {bc_configs['table_name']} WHERE {bc_configs['column6']} = {pin}"
    bc_cursor.execute(query)
    result = bc_cursor.fetchall()
        
    if result:
        return result[0][0]  # Return the first matching ClientID
    else:
        return None  # Return None if no matching PIN is found



###### Menus/Forms
def initialMenu():
    while True:
        try:
            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="KiBank Illuminaire", choice1="Open an Account", choice2="Client Management", choice3="Exit")
            initial_menu_choice = int(input("\tEnter your choice: "))

            if initial_menu_choice not in valid_choices:
                print()
                menu_notifier(message="[ERROR] You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return initial_menu_choice
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def clientManagement():
    while True:
        try:
            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="Client Management", choice1="List All Clients", choice2="Find a Client", choice3="Back")

            client_m_choice = int(input("\tEnter your choice: "))

            if client_m_choice not in valid_choices:
                print()
                menu_notifier(message="[ERROR] You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return client_m_choice
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def openAccount():
    while True:
        try:
            valid_choices = INITIAL_MENUS_VALID_CHOICES

            menu_layout(title="KiBank Illuminaire", choice1="First-time Client", choice2="Returning Client", choice3="Back")
            
            open_acc_choice = int(input("\tEnter your choice: "))


            if open_acc_choice not in valid_choices:
                print()
                menu_notifier(message="[ERROR] You can only choose [1], [2], or [0]. Please try again.")
                continue
            else:
                return open_acc_choice
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def create_client_menu():
    while True:
        try:
            print("====================================")
            print("\tClient Application Form")
            print("====================================")
            print()
            desired_id = int(input("Enter your desired Client ID [XXXX]: "))

            is_dup = CLIENT_INSTANCE.is_duplicate_client_id(desired_id)

            if is_dup:
                surname = input("Enter your surname: ")
                fname = input("Enter your first name: ")
                contact_no = input("Enter your contact number: ")
                gmail = input("Enter your email address: ")
                pin = input("Enter your desired PIN number [XXXX]: ")
        
                return desired_id, surname, fname, contact_no, gmail, pin
            else:
                print()
                menu_notifier(message="[ERROR] You entered an existing Client ID. Please try again.")
                continue
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def bank_account_creation_form():
    while True:
        try:
            print("=====================================")
            print("    Bank Account Creation Form")
            print("=====================================")
            print()
            bank_acc_id = int(input(("Enter your desired Bank Account ID [XXXX]: ")))

            is_dup = ACCOUNT_INSTANCE.is_duplicate_account_id(bank_acc_id)
            if is_dup:
                balance = int(input(("Enter the balance: ")))
            else:
                print()
                menu_notifier(message="[ERROR] You entered an existing Account ID. Please try again.")
                continue

            return bank_acc_id, balance
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def client_verification():
    while True:
        try:
            print("=====================================")
            print("   Returning Client Verification")
            print("=====================================")
            print()
            user_ID = int(input("Enter your Client ID [XXXX]: "))
            user_PIN = int(input("Enter your Client PIN [XXXX]: "))

            # Check if ID and PIN exist in the database
            query = f"SELECT * FROM {bc_configs['table_name']} WHERE {bc_configs['column1']} = {user_ID} AND {bc_configs['column6']} = {user_PIN}"
            bc_cursor.execute(query)
            result = bc_cursor.fetchone()

            if result:
                return True, user_PIN
            else:
                print()
                print("=====================================")
                print()
                print("[ERROR] ID and PIN combination does not exist. Please try again.")
                print()
                decision = input("Press [Y/N] to try again or return: ").lower()
                if decision == 'y':
                    clear()
                    continue
                elif decision == 'n':
                    clear()
                    break
                
        except ValueError:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please enter a valid PIN.")
        except Exception as e:
            print()
            menu_notifier(message=f"[ERROR] An error occurred: {str(e)}")

def client_finding():
    while True:
        try:
            print("====================================")
            print("\t   Finding Client")
            print("====================================")
            print()
            client_id = int(input("Enter the Client ID: "))

            return client_id

        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def account_finding():
    while True:
        try:
            print("====================================")
            print("\t   Finding Account")
            print("====================================")
            print()
            account_id = int(input("Enter the Account ID: "))

            return account_id

        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def bank_acc_management_menu():
    while True:
        try:
            valid_choices = [0, 1, 2, 3, 4, 5, 6]
            
            clear()
            print("=======================================")
            print("          Account Management")
            print("=======================================")
            print()
            print("[1] Open a New Bank Account")
            print("[2] List All of Existing Accounts")
            print("[3] Find an Account")
            print("[4] Deposit to an Account")
            print("[5] Withdraw from an Account")
            print("[6] Delete an Account")
            print("[0] Out")
            print()
            print("=======================================")
            user_choice = int(input("Enter your choice: "))

            if user_choice not in valid_choices:
                print()
                menu_notifier(message="[ERROR] You can only choose numbers from [0] up to [5]. Please try again.")
                continue
            else:
                return user_choice
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def deposit_form():
    while True:
        try:
            print("====================================")
            print("\tDeposit to an Account")
            print("====================================")
            print()
            account_id = int(input("Enter the Account ID: "))
            deposit_amount = int(input("Enter the Deposit amount: "))
            print()
            print("====================================")
            print()

            return account_id, deposit_amount

        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def withdraw_form():
    while True:
        try:
            print("====================================")
            print("\tWithdraw from an Account")
            print("====================================")
            print()
            account_id = int(input("Enter the Account ID: "))
            withdraw_amount = int(input("Enter the Withdraw amount: "))
            print()
            print("====================================")
            print()
            
            successful = ACCOUNT_INSTANCE.withdraw(account_id, withdraw_amount)
            if successful:
                print()
                print("====================================")
                print()
                input("Press [ENTER] to continue...")
                break
            else:
                print()
                print("====================================")
                print()
                decision = input("Press [Y/N] to try again or return: ").lower()
                if decision == 'y':
                    clear()
                    continue
                elif decision == 'n':
                    clear()
                    break
        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue

def delete_account_form():
    while True:
        try:
            print("====================================")
            print("\tDelete an Account")
            print("====================================")
            print()
            account_id = int(input("Enter the Account ID: "))
            print()

            successful = ACCOUNT_INSTANCE.delete_account(account_id)
            if successful:
                print()
                print("====================================")
                print()
                input("Press [ENTER] to continue...")
                break
            else:
                print()
                print("====================================")
                print()
                decision = input("Press [Y/N] to try again or return: ").lower()
                if decision == 'y':
                    clear()
                    continue
                elif decision == 'n':
                    clear()
                    break

        except:
            print()
            menu_notifier(message="[ERROR] You entered an invalid input. Please try again.")
            continue



##### Query functions
def createAccount(bank_acc_id, balance, client_id):
    try:
        query = f"INSERT INTO {ba_configs['table_name']} ({ba_configs['column1']}, {ba_configs['column2']}, {ba_configs['column3']}) VALUES (%s, %s, %s)"

        ba_cursor.execute(query, (bank_acc_id, balance, client_id))
        ba_db.commit()

        return True
    
    except Exception as e:
        bc_db.rollback()

        print()
        print(f"Error executing query: {e}")
        print()

        return False

def createClient(id, surname, first_name, contact_no, gmail, pin):
    try:
        query = f"INSERT INTO {bc_configs['table_name']} ({bc_configs['column1']}, {bc_configs['column2']}, {bc_configs['column3']}, {bc_configs['column4']}, {bc_configs['column5']}, {bc_configs['column6']}) VALUES (%s, %s, %s, %s, %s, %s)"

        bc_cursor.execute(query, (id, surname, first_name, contact_no, gmail, pin))
        bc_db.commit()

        return True
    
    except Exception as e:
        bc_db.rollback()

        print()
        print(f"Error executing query: {e}")
        print()

        return False

def findAccount(acc_id):
    query = f"SELECT * FROM {ba_configs['table_name']} WHERE {ba_configs['column1']} = {acc_id}"
    ba_cursor.execute(query)
    result = ba_cursor.fetchall()

    return bool(result)

def findClient(client_id):
    query = f"SELECT * FROM {bc_configs['table_name']} WHERE {bc_configs['column1']} = {client_id}"
    bc_cursor.execute(query)
    result = bc_cursor.fetchall()

    return bool(result)



###### Main Function
def main():
    while True:
        clear()
        create_acc_or_client = initialMenu()

        if create_acc_or_client == 1:
            print("====================================")
            print()
            menu_notifier(message="[NOTICE] You selected [1] Open an Account. Please wait a second...")
            open_acc_or_client_m = openAccount()
            if open_acc_or_client_m == 0:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [0] Back. Going back to the previous screen...")
                continue

            elif open_acc_or_client_m == 1:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [1] First-time Client. Please wait a second...")

                desired_id, surname, fname, contact_no, gmail, pin = create_client_menu()

                client_successful = createClient(desired_id, surname, fname, contact_no, gmail, pin)

                if client_successful:
                    menu_notifier(message="Client creation successful.")

                    print("[NOTICE] Creating your First Bank Account")
                    print()
                    
                    bank_acc_id, balance = bank_account_creation_form()

                    bank_successful = createAccount(bank_acc_id, balance, desired_id)

                    if bank_successful:
                        menu_notifier(message="Account created successfully. Going back to the menu...")
                        continue

                    else:
                        menu_notifier(message="Account creation failed. Going back to the menu...")
                        continue

                else:
                    menu_notifier(message="Client creation failed. Going back to the menu...")
                    continue 

            elif open_acc_or_client_m == 2:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [2] Returning Client. Please wait a second...")

                PIN_verification, user_PIN = client_verification()

                if PIN_verification:
                    print()
                    print("=====================================")
                    print()
                    menu_notifier(message="Client Verification Successful. Please wait a second...")
                    
                    while True:
                        try:
                            client_id = get_clientID_by_PIN(user_PIN)
                            bank_acc_management_choice = bank_acc_management_menu()

                            if bank_acc_management_choice == 0:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [0] Out. Going back to menu...")
                                break

                            elif bank_acc_management_choice == 1:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [1] Open New Bank Account. Please wait a second...")

                                bank_acc_id, balance = bank_account_creation_form()

                                bank_successful = createAccount(bank_acc_id, balance, client_id)

                                if bank_successful:
                                    menu_notifier(message="Account created successfully. Going back to the menu...")
                                    continue

                                else:
                                    menu_notifier(message="Account creation failed. Going back to the menu...")
                                    continue
                            
                            elif bank_acc_management_choice == 2:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [2] List All of Existing Accounts. Please wait a second...")
                                ACCOUNT_INSTANCE = BankAccount()
                                ACCOUNT_INSTANCE.list_all_accounts()
                            
                            elif bank_acc_management_choice == 3:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [3] Find an Account. Please wait a second...")
                                acc_id = account_finding()
                                account_found = findAccount(acc_id)

                                if account_found:
                                    # Class instance
                                    ACCOUNT_INSTANCE = BankAccount(id=acc_id)
                                    print()
                                    print()
                                    print("\t   --- Results ---")
                                    print("====================================")
                                    print("\t    Account Found")
                                    print("====================================")
                                    print()
                                    ACCOUNT_INSTANCE.printDetails()
                                    print()
                                    print("====================================")
                                    input("      Press [ENTER] to Back")
                                    continue
                                else:
                                    print()
                                    print()
                                    print("\t   --- Results ---")
                                    print("====================================")
                                    print()
                                    print("     This Account doesn't Exist")
                                    print()
                                    print("====================================")
                                    input("      Press [ENTER] to Back")
                                    continue
                            
                            elif bank_acc_management_choice == 4:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [4] Deposit. Please wait a second...") 

                                account_id, deposit_amount = deposit_form()

                                ACCOUNT_INSTANCE.deposit(account_id, deposit_amount)
                                
                                print()
                                print("====================================")
                                input("    Press [ENTER] to continue")

                            elif bank_acc_management_choice == 5:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [5] Withdraw. Please wait a second...")

                                withdraw_form()
                            
                            elif bank_acc_management_choice == 6:
                                print("=======================================")
                                print()
                                menu_notifier(message="[NOTICE] You selected [6] Delete an Account. Please wait a second...")

                                delete_account_form()
                                
                        except:
                            print("====================================")
                            print()
                            menu_notifier(message=f"[ERROR] You entered an invalid input. Please try again...")
                            continue
                
        elif create_acc_or_client == 2:
            print("====================================")
            print()
            menu_notifier(message="[NOTICE] You selected [2] Client Management. Please wait a second...")
            open_acc_or_client_m = clientManagement()
            
            if open_acc_or_client_m == 0:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [0] Back. Going back to the previous screen...")
                continue

            elif open_acc_or_client_m == 1:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [1] List All of the Clients. Please wait a second...")
                CLIENT_INSTANCE.list_all_clients()

            elif open_acc_or_client_m == 2:
                print("====================================")
                print()
                menu_notifier(message="[NOTICE] You selected [2] Find Client. Please wait a second...")
                id_client = client_finding()
                client_found = findClient(id_client)

                if client_found:
                    # Class instance
                    CLIENT_INSTANCE = BankClient(id=id_client)
                    print()
                    print()
                    print("\t   --- Results ---")
                    print("====================================")
                    print("\t\tClient Found")
                    print("====================================")
                    print()
                    CLIENT_INSTANCE.printDetails()
                    print()
                    print("====================================")
                    input("      Press [ENTER] to Back")
                    continue
                else:
                    print()
                    print()
                    print("\t   --- Results ---")
                    print("====================================")
                    print()
                    print("     This Client doesn't Exist")
                    print()
                    print("====================================")
                    input("      Press [ENTER] to Back")
                    continue
                
        elif create_acc_or_client == 0:
            print()
            print("[NOTICE] Thank you for trusting our bank!")
            print()
            sys.exit()



# Simply tells if the current Python file was ran
if __name__ == "__main__":
    main()