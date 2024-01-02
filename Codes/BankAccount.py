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

    def list_all_accounts(self):
        query = f"SELECT * FROM {self.ACCOUNT_CONFIG['table_name']}"
        result = self.execute_query(query)

        print("=" * 27)
        print("List of All Bank Accounts")
        print("=" * 27)

        if result:
            for account_details in result:
                self.id = account_details[0]
                client_id = self.getIDNumber()
                balance = self.getBalance()

                print(f"Account ID: {self.id}")
                print(f"Client ID: {client_id}")
                print(f"Balance: {balance}\n")
        else:
            print("No bank accounts found")

        print("=" * 27)
        input("Press [ENTER] to Back")


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

    def printDetails():
        pass

    def deposit():
        pass

    def withdraw():
        pass