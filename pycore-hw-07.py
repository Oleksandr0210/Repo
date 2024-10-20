from datetime import datetime, timedelta

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Insufficient arguments provided."
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Invalid key used."
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper


class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.name] = record

    def find(self, name):
        return self.records.get(name, None)

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now().date()
        end_date = today + timedelta(days=7)

        for record in self.records.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= end_date:
                    upcoming_birthdays.append({
                        "name": record.name.name,
                        "birthday": birthday_this_year
                    })
        
        return upcoming_birthdays


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name, phone)
        book.add_record(record)
        message = "Contact added."
    else:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    for phone in record.phones:
        if phone.value == old_phone:
            record.phones.remove(phone)
            record.add_phone(new_phone)
            return "Phone updated."
    
    return "Old phone number not found."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return ", ".join([phone.value for phone in record.phones])
    return "Contact not found."


@input_error
def show_all(args, book: AddressBook):
    if book.records:
        return "\n".join([f"{name}: {', '.join([phone.value for phone in record.phones])}" for name, record in book.records.items()])
    return "No contacts found."


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    
    record.add_birthday(birthday)
    return f"Birthday for {name} added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")
    return "Birthday not found."


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        return "\n".join([f"{item['name']} has birthday on {item['birthday']}" for item in upcoming])
    return "No birthdays in the next 7 days."


def parse_input(user_input):
    return user_input.split()


def main():
    book = AddressBook()
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
