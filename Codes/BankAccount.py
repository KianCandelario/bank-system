import mysql.connector as connector

class BankAccount:
    ### Setting configuration
    ACCOUNT_CONFIG = {
        "user" : "root",
        "host" : "localhost",
        "database_name" : "KiBankIlluminaire",
        "table_name" : "BankAccount",
        "column1" : "AccountID",
        "column2" : "Balance",
        "column3" : "ClientID"
    }

    ### Connector
    DATABASE = connector.connect(
        host = ACCOUNT_CONFIG["host"],
        user = ACCOUNT_CONFIG["user"],
        database = ACCOUNT_CONFIG["database_name"]
    )
    CURSOR = DATABASE.cursor()


    # Provided default values to make the arguments optional
    def __init__(self, id=0, initial_deposit=0):
        self.id = id
        self.initial_deposit = initial_deposit
    


    ### Auxillary functions
    def execute_query(self, query):
        self.CURSOR.execute(query)
        result = self.CURSOR.fetchall()
        return result
    
    def is_duplicate_account_id(self, account_id):
        query = f"SELECT * FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {account_id}"
        result = self.execute_query(query)
        return bool(result)
    
    def get_balance(self):
        query = f"SELECT {self.ACCOUNT_CONFIG['column2']} FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            return result[0][0]
        else:
            return None

    def delete_account(self, account_id):
        self.id = account_id
        current_balance = self.get_balance()

        if current_balance is not None:
            if current_balance == 0:
                # Delete account when balance is 0
                delete_query = f"DELETE FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {self.id}"
                self.execute_query(delete_query)
                self.DATABASE.commit()
                print(f"Account with ID {self.id} deleted successfully.")

                return True
            else:
                print(f"Current balance: {current_balance}")
                print("Cannot delete account with non-zero balance.")

                return False
        else:
            print("Account not found.")

    def list_all_accounts(self):
        query = f"SELECT * FROM {self.ACCOUNT_CONFIG['table_name']}"
        result = self.execute_query(query)

        print("====================================")
        print("    List of All Bank Accounts")
        print("====================================")
        print()

        if result:
            for account_details in result:
                account_id = account_details[0]
                client_id = account_details[2] 
                balance = account_details[1]

                print(f"Account ID: {account_id}")
                print(f"Client ID: {client_id}")
                print(f"Balance: {balance}")
                print()
        else:
            print("\tNo bank accounts found")

        print()
        print("====================================")
        input("\tPress [ENTER] to Back")

    def update_balance(self, account_id, new_balance):
        query = f"UPDATE {self.ACCOUNT_CONFIG['table_name']} SET {self.ACCOUNT_CONFIG['column2']} = {new_balance} WHERE {self.ACCOUNT_CONFIG['column1']} = {account_id}"
        self.execute_query(query)
        self.DATABASE.commit()



    ### Main functions
    def getBalance(self):
        query = f"SELECT {self.ACCOUNT_CONFIG['column2']} FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            return result[0][0]
        else:
            return None

    def getIDNumber(self):
        query = f"SELECT {self.ACCOUNT_CONFIG['column1']} FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            return result[0][0]
        else:
            return None

    def printDetails(self):
        query = f"SELECT * FROM {self.ACCOUNT_CONFIG['table_name']} WHERE {self.ACCOUNT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            account_details = result[0]
            print(f"Account ID: {account_details[0]}")
            print(f"Balance: ₱ {account_details[1]}")
            print(f"Client ID: {account_details[2]}")
        else:
            print("Client not found")

    def deposit(self, account_id, deposit_amount):
        self.id = account_id
        current_balance = self.getBalance()
        if current_balance is not None:
            new_balance = current_balance + deposit_amount
            self.update_balance(account_id, new_balance)
            print(f"Deposit of ₱ {deposit_amount} successful.")
            print(f"New balance: ₱ {new_balance}")
        else:
            print("Account not found")

    def withdraw(self, account_id, withdraw_amount):
        self.id = account_id
        current_balance = self.getBalance()
        if current_balance is not None:
            if current_balance >= withdraw_amount:
                new_balance = current_balance - withdraw_amount
                self.update_balance(account_id, new_balance)
                print(f"Withdrawal of ₱ {withdraw_amount} successful.")
                print(f"New balance: ₱ {new_balance}")
                return True
            else:
                print("Insufficient funds. Withdrawal unsuccessful.")
                return False
        else:
            print("Account not found. Withdrawal unsuccessful.")