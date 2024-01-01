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
    

    ### Auxillary function
    def execute_query(self, query):
        self.CURSOR.execute(query)
        result = self.CURSOR.fetchall()
        return result    


    def list_all_clients(self):
        query = f"SELECT * FROM {self.CLIENT_CONFIG['table_name']}"
        result = self.execute_query(query)

        print("====================================")
        print("\tList of All Clients")
        print("====================================")

        if result:
            for client_details in result:
                self.id = client_details[0]
                name = self.getName()
                id_number = self.getIDNumber()

                print(f"ClientID: {id_number}")
                print(f"Name: {name}")
                print()
        else:
            print("No clients found")

        print("====================================")
        input("\tPress [ENTER] to Back")


    ### Main Functions
    def getName(self):
        query = f"SELECT {self.CLIENT_CONFIG['column2']}, {self.CLIENT_CONFIG['column3']} FROM {self.CLIENT_CONFIG['table_name']} WHERE {self.CLIENT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            surname, firstname = result[0]
            return f"{surname}, {firstname}"
        else:
            return None


    def getIDNumber(self):
        query = f"SELECT {self.CLIENT_CONFIG['column1']} FROM {self.CLIENT_CONFIG['table_name']} WHERE {self.CLIENT_CONFIG['column1']} = {self.id}"
        result = self.execute_query(query)
        if result:
            return result[0][0]
        else:
            return None


    def printDetails(self):
        pass