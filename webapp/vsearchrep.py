"""This module is a repository vsearch web applicatoin

Available Function:
    - save_request:                 Store web reqeust in log database
    - get_log:                      Polls the log table for its entries
                                    and returns the results
    - total_number_of_requests:     Calculates the number of rows
                                    entered into the log database it
                                    represents the number of successfully
                                    returned answers to each request.
    - highest_letters_requested:    Calculates the highest requestd letter
                                    matching and the number of times they
                                    were requested
    - most_frequent_browser_used:   Calculates the most frequently used web
                                    browser and returns which browser was
                                    used and the number of times as a string
"""

from webapp.vsearchdatasource import UseDatabase


def most_frequent_browser_used() -> str:
    """Calculates the most frequently used web browser and
       returns which browser was used and the number of times
       as a string

       Returns:
           A string of number,browser combo
    """
    _SQL = """select count(browser_string) as 'count', browser_string
              from log
              group by browser_string
              order by count desc
              limit 1
           """
    with UseDatabase() as cursor:
        cursor.execute(_SQL)
        dictionary_output = cursor.fetchall()[0]
        return str(dictionary_output)


def highest_letters_requested() -> str:
    """Calculates the highest requestd letter matching and the number
       of times they were requested

       Returns:
           A string or number,letter combo
    """
    _SQL = """select count(letters) as 'count', letters
              from log
              group by letters
              order by count desc
              limit 1
           """
    with UseDatabase() as cursor:
        cursor.execute(_SQL)
        dictionary_output = cursor.fetchall()[0]
        return str(dictionary_output)


def total_number_of_requests() -> int:
    """"Calculates the number of rows entered into the log database it
        represents the number of successfully returned answers to each
        request.

        Returns:
            count of roows in the log table as an integer
    """
    _SQL = """select count(*) from log"""
    with UseDatabase() as cursor:
        cursor.execute(_SQL)
        number_of_rows = (cursor.fetchall()[0])[0]
    return str(number_of_rows)


def get_log() -> list:
    """Polls the log table for its entries and returns the results

    Returns:
       Rows of the tuplet (phrase, letters, ip, browser_string, and results).
    """
    _SQL = """select phrase, letters, ip, browser_string, results from log"""
    with UseDatabase() as cursor:
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    return contents


def save_request(req: 'flask request', res: str) -> None:
    """Store web reqeust in log database"""
    _SQL = """insert into log (phrase, letters, ip, browser_string, results) 
              values (%s, %s, %s, %s, %s)"""
    with UseDatabase() as cursor:
        cursor.execute(_SQL, (req.form['phrase']
                              , req.form['letters']
                              , req.remote_addr
                              , req.user_agent.browser
                              , res
                              )
                       )
