"""
    Defines Decorators.
"""

import time

from functools import wraps

from .auth import Auth
from .. import exceptions as exc


def retry(n, backoff, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param n: The number of times to repeat the wrapped function/method
    :param backoff:
    :param exceptions: Lists of exceptions that trigger a retry attempt
    """

    def decorator(func):
        @wraps(func)
        def new_fn(*args, **kwargs):
            attempt = 0
            while attempt < n:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if isinstance(e, exc.InvalidTokenError):
                        Auth().update_access_token()
                    time.sleep(backoff)
                    attempt += 1
            raise exc.RetryException('failed to execute %s despite retrying' % func.__name__)

        return new_fn

    return decorator
