from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client.cats_db
collection = db.cats


def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    result = collection.insert_one(cat)
    print(f"Кіт доданий з ID: {result.inserted_id}")


def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")


def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")


def add_feature_to_cat(name, new_feature):
    result = collection.update_one(
        {"name": name}, {"$push": {"features": new_feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{new_feature}' додана до кота {name}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")


def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям {name} видалений.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")


def delete_all_cats():
    result = collection.delete_many({})
    print(f"Всі коти видалені. Видалено записів: {result.deleted_count}")


def menu():
    while True:
        print("\n=== Меню ===")
        print("1. Додати нового кота")
        print("2. Показати всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("0. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            name = input("Ім'я кота: ")
            age = int(input("Вік кота: "))
            features = input("Характеристики (через кому): ").split(", ")
            create_cat(name, age, features)

        elif choice == "2":
            read_all_cats()

        elif choice == "3":
            name = input("Ім'я кота: ")
            read_cat_by_name(name)

        elif choice == "4":
            name = input("Ім'я кота: ")
            new_age = int(input("Новий вік: "))
            update_cat_age(name, new_age)

        elif choice == "5":
            name = input("Ім'я кота: ")
            new_feature = input("Нова характеристика: ")
            add_feature_to_cat(name, new_feature)

        elif choice == "6":
            name = input("Ім'я кота: ")
            delete_cat_by_name(name)

        elif choice == "7":
            confirm = input("Ви впевнені? (yes/no): ")
            if confirm.lower() == "yes":
                delete_all_cats()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    menu()