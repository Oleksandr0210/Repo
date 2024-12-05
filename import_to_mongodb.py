from pymongo import MongoClient
import json

client = MongoClient("your_mongodb_connection_string")
db = client["quotes_db"]
authors_collection = db["authors"]
quotes_collection = db["quotes"]


def import_authors():
    with open("authors.json", "r", encoding="utf-8") as f:
        authors = json.load(f)
        authors_collection.insert_many(authors)
        print("Дані про авторів успішно імпортовані.")


def import_quotes():
    with open("qoutes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
        quotes_collection.insert_many(quotes)
        print("Дані про цитати успішно імпортовані.")


def main():
    import_authors()
    import_quotes()


if __name__ == "__main__":
    main()