# 3 МОДУЛЬ В PYTHON CORE 2.0. ДОСТУПНІ НАСТУПНІ ЗАВДАННЯ:
# # ПЕРШЕ ЗАВДАННЯ

import datetime

def get_days_from_today(date='2023-10-09'):

    gotten_date = datetime.date(date)
    current_date = datetime.date.today()
    difference_date = current_date - gotten_date
    return date

# ДРУГЕ ЗАВДАННЯ

import random

def get_numbers_ticket(min=1, max=49, quantity=6):
    min = input("Enter any number from 1 to 10: ")
    min = int(min)

    max = input("Enter maximum number not more than 1000: ")
    max = int(max)

    quantity = input("Enter quantity of numbers you want to obtain: ")
    quantity = int(quantity)

    return min, max, quantity

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# ТРЕТЄ ЗАВДАННЯ

import re

mobilize_phone_numbers = [
    "+380501233234",
    "+380503451234",
    "+380508889900",
    "+380501112222",
    "+380501112211"
]

sanitized_phone_number = [mobilize_phone_numbers]
print("Normalize phone numbers for SMS:", sanitized_phone_number)
