class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise Exception("no more than 1 og that class")
    def __repr__(self):
        return f"Connection to DB {self.database_name})"

    
conn = DatabaseConnection("account_info.db")
print(conn)
