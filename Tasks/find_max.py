import sys


def io_find_max_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(func(*args, **kwargs))
    return wrapper


@io_find_max_decorator
def find_max(*args):
    lst = args[0]
    m = 1 - sys.maxsize
    for n in lst:
        if n > m:
            m = n
    return m


find_max([1, 2, 3])

