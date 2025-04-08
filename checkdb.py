import sqlite3
conn = sqlite3.connect('db.sqlite3')  # Замініть на шлях до вашого SQLite файлу
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # Наприклад, щоб побачити всі таблиці
tables = cursor.fetchall()
print(tables)

# Для кожної таблиці отримуємо і виводимо всі дані
for table in tables:
    table_name = table[0]
    print(f"Таблиця: {table_name}")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("-" * 50)  # Розділювач між таблицями


cursor.execute("PRAGMA table_info(shop_category);")
# Отримання результатів
columns = cursor.fetchall()

# Виведення результатів
for column in columns:
    print(column)


print(f"Таблиця: shop_product")

cursor.execute("PRAGMA table_info(shop_product);")
# Отримання результатів
columns = cursor.fetchall()

# Виведення результатів
for column in columns:
    print(column)


conn.close()
