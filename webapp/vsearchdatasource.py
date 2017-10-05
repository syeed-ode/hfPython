"""This module handles interaction with backend data store

Built specifically for the vsearch web application.  This module holds log
table specifics and should not be inherited.
"""
from mysql.connector import InterfaceError, connect, OperationalError, ProgrammingError

from webapp.vsearchexceptions import VSearchDataSourceError, VSearchCredentialsError, VSearchSQLError


class UseDatabase:
    def __init__(self) -> None:
        pass

    def __enter__(self) -> 'cursor':
        dbinfo = {'host': '127.0.0.1',
                  'user': 'vsearch',
                  'password': 'vsearchpasswd',
                  'database': 'vsearchlogDB',
                  }
        try:
            self.connection = connect(**dbinfo)
            self.cursor = self.connection.cursor()
            return self.cursor
        except ProgrammingError as error:
            raise VSearchCredentialsError('Username/Password issues' + str(error))
        except OperationalError as error:
            raise VSearchDataSourceError('Something went wrong: ', str(error))
        except InterfaceError as error:
            raise VSearchDataSourceError('Is you database up and running? I\'m receiving a:  '
                                         + str(error))

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is ProgrammingError:
            raise VSearchSQLError('\'with\' suite threw error', str(exc_value))
        elif exc_type:
            raise VSearchDataSourceError(exc_value)
