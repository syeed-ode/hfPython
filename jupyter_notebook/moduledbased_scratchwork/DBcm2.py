import mysql.connector


class UseDatabase:
    def __init__(self, dbconfiguration: dict) -> None:
        self.configuration = dbconfiguration

    def __enter__(self) -> 'cursor':
        self.connect = mysql.connector.connect(**self.configuration)
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.cursor.commit()
        self.cursor.close()
        self.connect.close()