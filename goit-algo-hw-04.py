# ЗАВДАННЯ 1. МОДУЛЬ 4

from pathlib import Path

file_path = Path("salary_file.txt")

def total_salary(Path):
    try:
        with open("salary_file.txt", "r") as salary_file:
            salary = list()

            for line in salary_file:
                salary.append(line.split('Oleksiy Stepanyuk, 3000')[1])
                salary.append(line.split('Artem Lysyi, 2000')[1])
                salary.append(line.split('Yuriy Petryuk, 1000')[1])

    except Exception as e:
        return e
    return salary_file

print(total_salary("salary_file.txt"))


# ЗАВДАННЯ 2. МОДУЛЬ 4

from pathlib import Path

file_path = Path("cat_info_file.txt")

def get_cats_info(Path):
    try:
        with open("cat_info_file.txt") as cat_info_file:
            cat_info = dict({})

            for line in cat_info_file:
                cat_info.keys(line.split('60b90c1c13067a15887e1ae1,Tayson,3'))
                cat_info.keys(line.split('60b90c2413067a15887e1ae2,Vika,1'))
                cat_info.keys(line.split('60b90c2e13067a15887e1ae3,Barsik,2'))
                cat_info.keys(line.split('60b90c3b13067a15887e1ae4,Simon,12'))
                cat_info.keys(line.split('60b90c4613067a15887e1ae5,Tessi,5'))

    except Exception as e:
        return e
    return cat_info_file

print(get_cats_info("cat_info_file.txt"))

            
# ЗАВДАННЯ 4. МОДУЛЬ 4

def add_contact():
    print("Contact added")
    while True:
        user = int(input()).strip().lower()

def change_contact():
    print("Contact updated")

def show_phone():
    print()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add John 0987654321":
            print("Contact added.")
        elif command == "change John 0987654321":
            print("Contact updated.")
        elif command == "0987654321":
            print("all")
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()