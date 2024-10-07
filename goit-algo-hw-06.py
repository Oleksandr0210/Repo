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

    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        return phone

    def remove_phone(self, phone):
        return phone

    def edit_phone(self, phone):
        return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_record(self, record):
        return record

class AddressBook(UserDict):
    def add_record(self, record):
        self.data = record

    def find(self, name):
        return Record(name)

    def delete(self, name):
        return name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def find_phone(self):
        pass


book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
jane_record = Record("Jane")    
jane_record.add_phone("9876543210")
jane_record.add_phone("0987654342")
book.add_record(jane_record)
print(book)

john = book.find("John")
jane = book.find("Jane")
print(john)
print(jane)

found_phone = john.add_phone("5555555555")
print(f"{john.name}: {found_phone}")
found_phone = jane.add_phone("1234567890")
print(f"{jane.name}: {found_phone}")