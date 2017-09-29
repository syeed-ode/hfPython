"""This module handles interaction with backend data store

Built specifically for the vsearch web application.  This module holds log
table specifics and should not be inherited.
"""

from mysql.connector import connect


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.connection = connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_request(self, req: 'flask request', res: str) -> None:
        """Store web reqeust in log database"""
        dbconfig = dict(host='127.0.0.1', user='', password='', database='vsearchlogDB')
        _SQL = """insert into log (phrase, letters, ip, browser_string, results) 
                  values (%s, %s, %s, %s, %s)"""
        self.cursor.execute(_SQL, (req.form['phrase']
                              , req.form['letters']
                              , req.remote_addr
                              , req.user_agent.browser
                              , res
                              )
                       )
