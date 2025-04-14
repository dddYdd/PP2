import psycopg2
import csv
import os

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()

def insert_from_csv(filename):
    if not os.path.exists(filename):
        print("Файл не найден:", filename)
        return
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", row)
    conn.commit()
    print("Данные добавлены из CSV.")

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Добавлено.")

def update_user():
    name = input("Кого изменить (имя): ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый номер: ")
    cur.execute("UPDATE PhoneBook SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, name))
    conn.commit()
    print("Обновлено.")

def query_data():
    start = input("Имена, начинающиеся с: ")
    cur.execute("SELECT * FROM PhoneBook WHERE name LIKE %s", (start + '%',))
    rows = cur.fetchall()
    if not rows:
        print("Ничего не найдено.")
    for row in rows:
        print(row)

def delete_user():
    name = input("Кого удалить (имя): ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    conn.commit()
    print("Удалено.")

def menu():
    while True:
        print("""
1. Insert from CSV
2. Insert from console
3. Update user
4. Query users
5. Delete user
6. Exit
        """)
        choice = input("Выбор: ")
        if choice == "1":
            insert_from_csv("Lab10/contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

create_table()
menu()
cur.close()
conn.close()

