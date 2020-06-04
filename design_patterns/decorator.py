import time


"""Decorator function that prints argument and keyword
arguments sent to a function, along with the function's
runtime"""
def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print(
            "Calling {0} with {1} and {2}".format(
                func.__name__, args, kwargs
            )
        )
        """Decorated function is run with args and kwargs
        passed to it"""
        return_value = func(*args, **kwargs)
        print(
            "Executed {0} in {1}ms".format(
                func.__name__, time.time() - now
            )
        )
        """wrapper function returns wrapped function"""
        return return_value
    """decorator returns wrapper function"""
    return wrapper

@log_calls
"""Decorator applied to function"""
def test1(a, b, c):
    print("\ttest1 called")

@log_calls
def test2(a, b):
    print("\ttest2 called")

@log_calls
def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)