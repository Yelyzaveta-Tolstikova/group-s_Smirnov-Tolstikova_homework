from time import time
from functools import wraps

def fibonacci_func(arg):
    if arg in (1, 2):
        return 1

    fib1 = fib2 = 1

    for arg in range(arg - 2):
        fib1, fib2 = fib2, fib1 + fib2 
        
    return fib2

print(fibonacci_func)

def decorator_func(some_func):

    @wraps(some_func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = some_func(*args, **kwargs)
        print(f'It took {str(time() - start_time)[:4]} seconds')

        return result

    return wrapper


@decorator_func
def fibonacci_func(arg):
    if arg in (1, 2):
        return 1

    fib1 = fib2 = 1

    for arg in range(arg - 2):
        fib1, fib2 = fib2, fib1 + fib2 
        
    return fib2


print(fibonacci_func)




