import sqlite3
from faker import Faker

conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

fake = Faker()

statuses = [('new',), ('in progress',), ('completed',)]
cursor.executemany("INSERT OR IGNORE INTO status (name) VALUES (?)", statuses)

for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))

for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.text()
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
        (title, description, status_id, user_id)
    )

conn.commit()
conn.close()
print("Database seeded successfully.")