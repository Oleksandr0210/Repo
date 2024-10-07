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
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        return phone

    def add_record(self, record):
        return record

class AddressBook(UserDict):
    def add_record(self, record):
        return record

    def find(self, name):
        return name


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