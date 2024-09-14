# ЗАВДАННЯ 1. МОДУЛЬ 5

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

print(caching_fibonacci())




# ЗАВДАННЯ 2. МОДУЛЬ 5



# ЗАВДАННЯ 4. МОДУЛЬ 5