"""This module provides code to assure a user has properly authnticated
   prior to provide access to protected resources.
"""

from flask import session
from functools import wraps

LOGGED_IN = 'logged_in'


def verify_logged_in_user(func: 'function') -> 'function':
    @wraps(func)
    def wrapper(*args, **kwargs):
        if LOGGED_IN in session:
            return func(*args, **kwargs)
        return 'You are not logged in'
    return wrapper
