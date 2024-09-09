# ЗАВДАННЯ 1. МОДУЛЬ 3

from datetime import datetime

def get_days_from_today(date):
    last_date = datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.today().date()
    difference_date = today_date - last_date
    return difference_date.days

print(get_days_from_today('2023-10-10'))

try:
    get_days_from_today(date='2023-10-10')
except Exception as e:
    print(e)


# ЗАВДАННЯ 2. МОДУЛЬ 3

import random

def get_numbers_ticket(min=10, max=20, quantity=5):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return ()
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_numbers)
    

print(get_numbers_ticket(10, 20, 5))
lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Your lottery numbers are:", lottery_numbers)