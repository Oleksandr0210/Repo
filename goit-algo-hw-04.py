# ЗАВДАННЯ 1. МОДУЛЬ 4

def total_salary(path):
    try:
        with open(path, "salary_file.txt", "r", encoding='utf-8') as salary_file:
            salary = list()

            for line in salary_file:
                salary.append(line.split(','))
                salary.append(line.split(','))
                salary.append(line.split(','))

                if len(salary) > 1 and salary[1].isdigit():
                    salary = int(salary[1])
                    total += salary
                    count += 1
        if count == 0:
            return (0, 0)
            
        average_salary = total / count
        return (total, average_salary)

    except FileNotFoundError:
        return f"Файл не знайдений."
    except Exception as e:
        return f"Сталася помилка: {e}"

print(total_salary("salary_file.txt"))


# ЗАВДАННЯ 2. МОДУЛЬ 4

def get_cats_info(path):
    cat_info_list = []

    try:
        with open(path, "cat_info_file.txt", "r", encoding='utf-8') as cat_info_file:
            cat_info = dict({})

            for line in cat_info_file:
                cat_info.keys(line.split(','))

                if len(cat_info) == 15:
                    cat_info = [{"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
                        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
                        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
                        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
                        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
                    ]
        return cat_info_list
    except FileNotFoundError:
        return f"Файл не знайдений."
    except Exception as e:
        return f"Сталася помилка: {e}"

print(get_cats_info("cat_info_file.txt"))

            
# ЗАВДАННЯ 4. МОДУЛЬ 4


contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def parse_input(user_input):
    parts = user_input.lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                add_contact(name, phone)
            else:
                print("Error: Please provide both name and phone number.")
        
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                change_contact(name, new_phone)
            else:
                print("Error: Please provide both name and new phone number.")
        
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                show_phone(name)
            else:
                print("Error: Please provide a name.")
        
        elif command == "all":
            show_all()
        
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
