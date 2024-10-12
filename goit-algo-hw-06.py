# ТЕХНІЧНЕ ЗАВДАННЯ. МОДУЛЬ 6

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_ob = self.find_phone(phone)
        if phone_ob:
            self.phones.remove(phone_ob)
        else:
            print(f"Phone {phone} not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_ob = self.find_phone(old_phone)
        if phone_ob:
            self.add_phone(new_phone)
        else:
            raise ValueError(f"Phone {old_phone} not found to edit.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = ', '.join([str(phone) for phone in self.phones])
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact {name} not found.")

    def __str__(self):
        return '\n'.join([str(record) for record in self.data.values()])


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