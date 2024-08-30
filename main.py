# 3 МОДУЛЬ В PYTHON CORE 2.0. ДОСТУПНІ НАСТУПНІ ЗАВДАННЯ:
# # ПЕРШЕ ЗАВДАННЯ

import datetime

def get_days_from_today(date):

    today_date = datetime.datetime(year=2024, month=8, day=14)
    future_date = datetime.datetime(year=2024, month=10, day=10)

    difference_date = future_date - today_date

    print(difference_date)


# ДРУГЕ ЗАВДАННЯ

import random

def get_numbers_ticket(min, max, quantity):

    number_tickets = (3, 16, 34, 48, 22, 8)
    lottery_numbers = random.choices(number_tickets, k=1)
    print("Your lottery number is...", lottery_numbers)

# ТРЕТЄ ЗАВДАННЯ

import re

def normalize_phone(phone_number):

    mobilize_phone_numbers = [
    "+380501233234",
    "+380503451234",
    "+380508889900",
    "+380501112222",
    "+380501112211"
    ]

    sanitized_phone_number = [mobilize_phone_numbers]
    print("Normalize phone numbers for SMS:", sanitized_phone_number)

