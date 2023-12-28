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

    def __init__(self, id, name, account):
        self.id = id
        self.name = name
        self.account = account
    
    def getName():
        pass

    def getIDNumber():
        pass

    def getAccount():
        pass

    def printDetails():
        pass