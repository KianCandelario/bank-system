import mysql.connector as connector

class BankClient:
    ### Setting configuration
    CLIENT_CONFIG = {
        "user" : "root",
        "host" : "localhost",
        "database_name" : "KiBankIlluminaire",
        "table_name" : "BankClient",
        "column1" : "ClientID",
        "column2" : "Surname",
        "column3" : "FirstName",
        "column4" : "ContactNo",
        "column5" : "Gmail",
        "column6" : "PIN"
    }

    ### Connector
    DATABASE = connector.connect(
        host = CLIENT_CONFIG["host"],
        user = CLIENT_CONFIG["user"],
        database = CLIENT_CONFIG["database_name"]
    )
    CURSOR = DATABASE.cursor()

    # Provided default values to make the arguments optional
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name
    
    def list_all_clients(self):
        try:
            print("====================================")
            print("\tList of All the Clients")
            print("====================================")
            print()

            # Retrieve all clients from the database
            query = f"SELECT {self.CLIENT_CONFIG['column1']}, {self.CLIENT_CONFIG['column2']}, {self.CLIENT_CONFIG['column3']} FROM {self.CLIENT_CONFIG['table_name']}"
            self.CURSOR.execute(query)
            results = self.CURSOR.fetchall()

            for result in results:
                client_id, surname, first_name = result
                print(f"Client ID: {client_id}")
                print(f"Name: {surname}, {first_name}\n")
            
            print()
            print("====================================")
            input("\tPress [ENTER] to go back.")

        except Exception as e:
            print(f"[ERROR] An error occurred: {str(e)}")
        finally:
            # Close the cursor after execution
            self.CURSOR.close()
            # Reopen the cursor to avoid issues in subsequent queries
            self.CURSOR = self.DATABASE.cursor()

    def getName():
        pass

    def getIDNumber():
        pass

    def getAccount():
        pass

    def printDetails():
        pass