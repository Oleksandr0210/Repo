import pickle
from datetime import datetime, timedelta
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits.")


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name, phone=None, birthday=None, favorite=False):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.favorite = favorite
        if phone:
            self.add_phone(phone)
        if birthday:
            self.add_birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.add_phone(new_phone)
                return "Phone updated."
        return "Old phone number not found."

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __repr__(self):
        phones = ", ".join([phone.value for phone in self.phones])
        birthday = self.birthday.value if self.birthday else "No birthday"
        return f"Record(Name: {self.name.value}, Phones: {phones}, Birthday: {birthday}, Favorite: {self.favorite})"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted."
        return f"Contact {name} not found."

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now().date()
        end_date = today + timedelta(days=7)

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = datetime.strptime(
                    record.birthday.value, "%d.%m.%Y").date().replace(year=today.year)

                if birthday_this_year.weekday() == 5:
                    birthday_this_year += timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    birthday_this_year += timedelta(days=1)

                if today <= birthday_this_year <= end_date:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError) as e:
            return str(e)
    return inner


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
    save_data(book)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."

    message = record.edit_phone(old_phone, new_phone)
    save_data(book)
    return message


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return ", ".join([phone.value for phone in record.phones])
    return "Contact not found."


@input_error
def show_all(args, book: AddressBook):
    if book.data:
        result = []
        for name, record in book.data.items():
            phones = ", ".join([phone.value for phone in record.phones])
            birthday = record.birthday.value if record.birthday else "No birthday"
            result.append(f"{name}: Phones: {phones}; Birthday: {
                          birthday}; Favorite: {record.favorite}")
        return "\n".join(result)
    return "No contacts found."


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_birthday(birthday)
    save_data(book)
    return f"Birthday for {name} added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value
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
    book = load_data()
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

        elif command == "delete":
            print(book.delete(args[0]))
            save_data(book)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
