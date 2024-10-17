from datetime import datetime

contacts = {}

class AddressBook:
    def __init__(self, book):
        self.book = book


class Field:
    def __init__(self, value):
        self.value = value
        

class Name:
    def __init__(self, name):
        self.name = name
        

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
      
  
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, new_phone, *_ = args
    record = book.find(name)
    message = "Contact updated"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact updated."
    if new_phone:
        record.add_phone(new_phone)
    return message
   
   
@input_error 
def show_phone(args, book: AddressBook):
    phone = args[0]
    record = book.find(phone)
    message = "Contact found"
    if record is None:
        record = Record(phone)
        book.add_record(record)
        message = "Contact found."
    else:
        message = "Contact not found"
    return message
    

@input_error
def show_all(*args, **kwargs):
    if contacts:
        return "\n".join([f"{name.format()}: {phone}" for name, phone in contacts.items()])
    else:
        return "Enter the argument for the command."
    

@input_error
def add_birthday(args):
    name, birthday = args
    contacts[name] = birthday
    return "Birthday added."
    
    
@input_error
def show_birthday(args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Enter the argument for the command."

    
@input_error
def birthdays(args, book: AddressBook):
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
    book = AddressBook(Record)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")
            
if __name__ == "__main__":
    main()