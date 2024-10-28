import pickle


class Person:
    def __init__(self, name, email, phone, favorite: bool = False):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Person({self.name}, {self.email}, {self.phone}, Favorite: {self.favorite})"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Person):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

    def __repr__(self):
        return f"AddressBook({self.contacts})"


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    address_book = load_data()

    print("Адресна книга при запуску:")
    address_book.display_contacts()

    new_contact = Person("John Doe", "john.doe@example.com",
                         "(123) 456-7890", favorite=True)
    address_book.add_contact(new_contact)

    print("\nПісля додавання нового контакту:")
    address_book.display_contacts()

    save_data(address_book)
    print("\nДані збережено.")


if __name__ == "__main__":
    main()
