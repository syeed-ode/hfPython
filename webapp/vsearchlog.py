"""This module handles the logging of requests to our vsearch4web webb application

Avalilable functions:
    read_log:           Returns the contents of the log file as a list of lists.
    log_request:        Processes input requests from Flask and responses and logs
                        the form, remote_address, the browser type and results
                        from vsearch4web method. It overrides the seperataor
                        keyword, verses the end keyword to place everything on one
                        line.
    read_unformatted_log:   Returns the contents of the log file as is: string
                        representation of a list of lists.
    log_full_request:   Processes input requests from Flask and responses and logs
                        all of the attributes, methods and classes of the Flask
                        request object.
    log_request_attr_overriding_end_keyword:   Processes input requests from Flask
                        and responses and logs the form, remote_address, the
                        browser type and results from vsearch4web method.
"""
from flask import escape


FILE_NAME = '/Users/syeedode/python_projects/hfPython/webapp/vsearch.log'


def read_log() -> 'list':
    """Reads the current log file and returns the results

    Returns:
       All of the contents of the log as a string.
    """
    with open(FILE_NAME) as log:
        contents = list()
        for line in log:
            contents.append(list())
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return contents


def log_request(req: 'flask_request', res: str) -> None:
    """Processes input requests from Flask and responses and
       logs the form, remote_address, the browser type and results
       from vsearch4web method. It overrides the seperataor keyword,
       verses the end keyword to place everything on one line.

       Args:
           req:     flask.request object
           res:     result from vsearch4web
       """
    with open(FILE_NAME, 'a') as logger:
        print(req.form, req.remote_addr, req.user_agent, res, file=logger, sep='|')


def log_entry(*args) -> None:
    s = str(args)
    print(s)
    with open(FILE_NAME, 'a') as logger:
        print(s, file=logger)


def read_unformatted_log() -> str:
    """Reads the current log file and returns the results

    Returns:
       All of the contents of the log as a string.
    """
    with open(FILE_NAME) as log:
        contents = list()
        for line in log:
            contents.append(list())
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return str(contents)


def log_request_attr_overriding_end_keyword(req: 'flask_request', res: str) -> None:
    """Processes input requests from Flask  and responses and logs the
       form, remote_address, the browser type and results from vsearch4web
       method.

       Args:
           req:     flask.request object
           res:     result from vsearch4web
       """
    with open(FILE_NAME, 'a') as logger:
        print(req.form, file=logger, end='|')
        print(req.remote_addr, file=logger, end='|')
        print(req.user_agent, file=logger, end='|')
        print(res, file=logger)


def log_full_request(req: 'flask_request', res: str) -> None:
    """Processes input requests from Flask and responses and logs
       them with the open context manager.

       Args:
           req:     flask.request object
           res:     result from vsearch4web
       """
    with open(FILE_NAME, 'a') as logger:
        print(str(dir(req)), res, file=logger)
