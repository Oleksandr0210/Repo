# ЗАВДАННЯ 1. МОДУЛЬ 3

from datetime import datetime

def get_days_from_today(date):
    last_date = datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.today().date()
    difference_date = today_date - last_date
    return difference_date.days

print(get_days_from_today('2023-10-10'))


# ЗАВДАННЯ 2. МОДУЛЬ 3

import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = [4, 15, 23, 28, 37, 45]
    return lottery_numbers
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers are:", lottery_numbers)