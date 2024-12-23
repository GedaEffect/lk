import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())

# Проверка пароля
def check_password(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Добавление пользователя (для тестов или ручного управления)
def add_user(username, password):
    hashed_password = hash_password(password).decode('utf-8')
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(f"Пользователь {username} успешно добавлен.")
    except sqlite3.IntegrityError:
        print(f"Ошибка: Пользователь {username} уже существует.")
    finally:
        conn.close()