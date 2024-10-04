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

import re

from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r'\d+\.\d+|\d+', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


# ЗАВДАННЯ 4. МОДУЛЬ 5

contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error
def add_contact(args):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Enter the argument for the command."
    
@input_error
def change_contact(args):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Enter the argument for the command."

@input_error
def show_phone(args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Enter the argument for the command."

@input_error
def show_all(*args, **kwargs):
    if contacts:
        return "\n".join([f"{name.format()}: {phone}" for name, phone in contacts.items()])
    else:
        return "Enter the argument for the command."

@input_error
def parse_input(user_input):
    parts = user_input.lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            print(add_contact(args))

        elif command == "change":
            print(change_contact(args))
        
        elif command == "phone":
            print(show_phone(args))
        
        elif command == "all":
            print(show_all(args))
        
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
