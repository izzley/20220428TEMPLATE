"""
Decorator which returns run time for a function
This decorator is an alternative to using the python timeit module. 
"""
from functools import wraps
from loguru import logger
from time import perf_counter

def timing(func):
    """Runtime wrapper for functions. Also returns args and kwargs

        Args:
            func (function): function to time from start to finish

        Returns:
            func_meta (str): function performance metadata including ars and kwargs
    """
    @wraps(func)
    def wrap(*args, **kwargs):
        time_start = perf_counter()
        # run the func
        func_meta = func(*args, **kwargs)
        time_end = perf_counter()
        run_time = time_end - time_start

        # @NOTE: !r will return repr of func and :.8f is 8 decimal places
        all_meta = f"func: {func.__name__!r}, args:{[args, kwargs]}, time taken: {run_time:.8f}"
        logger.debug(all_meta)
        return func_meta
    return wrap