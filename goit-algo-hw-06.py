# ТЕХНІЧНЕ ЗАВДАННЯ. МОДУЛЬ 6


from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record:
    def __init__(self, name):
        self.name = name
        self.name = Name(name)
        self.phones = []

    def __init__(self, name):
        self.name = name

    def add_phone(self, phone):
        return phone

    def remove_phone(self, phone):
        self.phone = phone

    def edit_phone(self, phone):
        return phone

    def find_phone(self, phone):
        self.phone = phone
        return phone

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, data):
        self.data = data

    def find(self, name):
        self.name = name
        return Record

    def delete(self, name):
        return name

    def __init__(AddressBook):
        pass


book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)     
print(book)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")