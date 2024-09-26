# ЗАВДАННЯ 1. МОДУЛЬ 4

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding='utf-8') as salary_file:
            for line in salary_file:
                parts = line.strip().split(',')

                if len(parts) > 1 and parts[1].isdigit():
                    salary = int(parts[1])
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
        with open(path, "r", encoding='utf-8') as cat_info_file:
            cat_info = dict({})

            for line in cat_info_file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cat_info_list.append(cat_info)
        return cat_info_list
    except FileNotFoundError:
        return f"Файл не знайдений."
    except Exception as e:
        return f"Сталася помилка: {e}"

print(get_cats_info("cat_info_file.txt"))

            
# ЗАВДАННЯ 4. МОДУЛЬ 4

contacts = {}

def add_contact(args):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Error: Please provide both name and phone number."

def change_contact(args):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Error: Please provide both name and new phone number."

def show_phone(args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Error: Please provide a name."

def show_all(args):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

def parse_input(user_input):
    parts = user_input.lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        
        elif command == "add":
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
