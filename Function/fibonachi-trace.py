from functools import wraps


def trace(func):
    func.count = 0
    @wraps(func)
    def call(*args, **kwargs):
        print("__" * func.count +  '--> {} ({})'.format(func.__name__, args[0]))
        func.count += 1
        k = func(*args, **kwargs)
        func.count -= 1
        print("__" * func.count +  '<-- {} ({}) == ({})'.format(func.__name__, args[0], k))
        return k
    return call

@trace
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(3))