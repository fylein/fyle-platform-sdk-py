"""
    Defines Decorators.
"""

import time

from .auth import Auth
from .. import exceptions as exc

def retry(n, backoff, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param times: The number of times to repeat the wrapped function/method
    :type times: Int
    :param Exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """
    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < n:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if exc.InvalidTokenError in exceptions:
                        Auth().update_access_token()
                    time.sleep(backoff)
                    attempt += 1
            raise exc.RetryException('failed to execute %s despite retrying' % (func))
        return newfn
    return decorator