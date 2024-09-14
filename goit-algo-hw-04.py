# ЗАВДАННЯ 1. МОДУЛЬ 4

def total_salary(path):
    with open('salary_file.txt') as salary_file:
        developer_salary_date = {
            'name1': 'Alex Korp', 'total_salary1': 3000,
            'name2': 'Nikita Borisenko', 'total_salary2': 2000,
            'name3': 'Sitarama Raju', 'total_salary3': 1000,
        }
        return developer_salary_date.split(',')
    return total_salary

first_sum = 3000
second_sum = 2000
third_sum = 1000

total_sums = first_sum + second_sum + third_sum
print(total_sums)

total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary is: {total}, Average salary is: {average}")


# ЗАВДАННЯ 2. МОДУЛЬ 4

def get_cats_info(path):
    with open("path/to/cat_file.txt") as cat_info_file:
        cat_info = [
            {"id1": "60b90c1c13067a15887e1ae1", "name1": "Tayson", "age1": "3"},
            {"id2": "60b90c2413067a15887e1ae2", "name2": "Vika", "age2": "1"},
            {"id3": "60b90c2e13067a15887e1ae3", "name3": "Barsik", "age3": "2"},
            {"id4": "60b90c3b13067a15887e1ae4", "name4": "Simon", "age4": "12"},
            {"id5": "60b90c4613067a15887e1ae5", "name5": "Tessi", "age5": "5"},
        ]
        return cat_info.split(',')
    return cat_info_file

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)


# ЗАВДАННЯ 4. МОДУЛЬ 4

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add John 1234567890":
            print("Contact added")
        elif command == "change John 0987654321":
            print("Conctact updated")
        elif command == "phone John":
            print("0987654321")
        elif command == "all":
            print("all")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
