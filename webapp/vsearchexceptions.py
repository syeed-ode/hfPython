"""This module holds all application exceptions for the vsearch project.
"""


class VSearchDataSourceError(Exception):
    pass


class VSearchCredentialsError(VSearchDataSourceError):
    """Raised when a pProgrammingError occurs within the __enter__ method.
       It occurs when you provide an incorrect username or password from
       the code to the backend DB.
    """
    pass


class VSearchSQLError(VSearchDataSourceError):
    """Raised when a ProgrammingError is reported to the __exit__ method.
       by the operations of the 'with' suite.
    """
    pass
