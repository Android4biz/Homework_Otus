from time import time
from timeit import default_timer as timer
from functools import wraps

# Квадраты
def func(*n, pow=2):
    return [i**pow for i in n]


print(func(1, 2, 3, pow=2))

# Функция map
values = [1, 2, 3, 4, 5, 6, 7, 8]
Map = map(func, values)
print(list(Map))


# Функция поиска простых чисел
def is_prime(n):
    d = 2
    if n <= 1:
        return
    while n % d != 0:
        d += 1
    return d == n

print(is_prime(15))


r = list(range(1, 10))
prime_number = filter(is_prime, r)
print(list(prime_number))



# Функция нахожденя кратных 2, 3 и возврат списка
def numbers(*args, even=2):
    if even==0:
        return
    else:
        return [i for i in args if i % even==0]

print(numbers(1, 2, 3, 4, 5, 6, 7, even=2))



# Декоратор замера времени выполнения функции простых чисел
def decorator_timer(func):
    @wraps(func)
    def wraps_decorator(*args, **kwargs):
        start = timer()
        print('Время старта функции {}'.format(start))
        func(*args, **kwargs)
        end = timer()
        result = func(*args, **kwargs)
        print('Время концовки {}'.format(end))
        print('Разница {}'.format(end - start))
        return result
    return wraps_decorator


@decorator_timer
def is_prime(n):
    d = 2
    if n <= 1:
        return
    while n % d != 0:
        d += 1
    return d == n


r = list(range(2, 10))
prime_number = filter(is_prime, r)
print(list(prime_number))

