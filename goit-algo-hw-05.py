# ЗАВДАННЯ 1. МОДУЛЬ 5

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))


# ЗАВДАННЯ 2. МОДУЛЬ 5

from typing import Callable

def generator_numbers(text: str):
    numbers = "1000.0", "27.45", "324.00"
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    yield sum(text, func)


text = generator_numbers(text="Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")