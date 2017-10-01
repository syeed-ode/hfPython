"""This module handles interaction with backend data store

Built specifically for the vsearch web application.  This module holds log
table specifics and should not be inherited.
"""

from mysql.connector import connect


class UseDatabase:
    def __init__(self) -> None:
        pass

    def __enter__(self) -> 'cursor':
        dbinfo = {'host': '127.0.0.1',
                  'user': 'vsearch',
                  'password': 'vsearchpasswd',
                  'database': 'vsearchlogDB',
                  }
        self.connection = connect(**dbinfo)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
