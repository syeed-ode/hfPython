"""This module evaluates various dynamic keyword argument operations

Available Functions:
    - decoe:
"""
import json


def decoe(data, default=dict()):
    """Demonstrates that 1) keyword args only get set once, when
       the function is pulled into memory.  Once set to something

    Args:
        data:       JSON data to decode
        default:    Value to return if decoding fails.  Defaults
                    to an empty dictionary.  However, because
                    Keywords only get loaded once, modifing the
                    dictionary after being called, permenently
                    modifies the refernce.
    """
    try:
        return json.loads(data)
    except ValueError:
        return default


def decode(data, default=None):
    """Demonstrates that 1) keyword args only get set once, when
       the function is pulled into memory.  Once set to something

    Args:
        data:       JSON data to decode
        default:    Value to return if decoding fails.  Defaults
                    to an empty dictionary.  However, because
                    Keywords only get loaded once, modifing the
                    dictionary after being called, permenently
                    modifies the refernce.
    """
    default = {} if default is None else default

    try:
        return json.loads(data)
    except ValueError:
        return default
