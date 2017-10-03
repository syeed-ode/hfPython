"""This module examines the benefit of using 'with' and 'contextmanager'
   instead of creating your own context manager.

Available Functions:
    -
 """
import logging
from contextlib import contextmanager


def my_function() -> 'None':
    """Prints out three levels of log messages.
    """
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


def command_line_runs() -> 'None':
    """Simulate what runs on the command line
    """
    my_function()


@contextmanager
def debug_logging(level: 'str') -> 'None':
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    print(old_level)
    logger.setLevel(level=level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def run_command_line() -> 'None':
    with debug_logging(logging.DEBUG):
        print('Inside with: ')
        my_function()

    print('After with statement')
    my_function()
