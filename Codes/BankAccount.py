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


    def __init__(self, id, initial_deposit):
        self.id = id
        self.initial_deposit = initial_deposit
    
    def getBalance():
        pass

    def getIDNumber():
        pass

    def printDetails():
        pass

    def deposit():
        pass

    def withdraw():
        pass