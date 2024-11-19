import sqlite3

# Подключаемся к базе данных (если её нет, она будет создана)
conn = sqlite3.connect('lk_degaeffect.db')
cursor = conn.cursor()

# Создаём таблицу для пользователей
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    job_title TEXT,
    access_level INTEGER NOT NULL,
    department TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,  -- Храните хэш пароля
    profile_picture TEXT DEFAULT NULL,
    phone_number TEXT DEFAULT NULL
)
''')

# Создаём таблицу для ролей (опционально, если роли задаются отдельно)
cursor.execute('''
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    access_level INTEGER NOT NULL -- Глобальный уровень доступа
)
''')

# Создаём таблицу для доступов к отделам
cursor.execute('''
CREATE TABLE IF NOT EXISTS department_access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    department TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
''')

# Создаём таблицу для отслеживания рабочего времени
cursor.execute('''
CREATE TABLE IF NOT EXISTS work_hours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    hours_worked REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
''')

# Создаём таблицу для уведомлений
cursor.execute('''
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    is_read BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно создана.")
