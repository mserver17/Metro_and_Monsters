import sqlite3
from faker import Faker
import random

# Конфигурация Faker
fake = Faker('ru_RU')

# Путь к файлу базы данных
db_file = 'DB\sqlite.db'

def create_tables():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Создаем таблицы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        character_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        job TEXT,
        town TEXT,
        strength INTEGER,
        agility INTEGER,
        endurance INTEGER,
        intelligence INTEGER,
        luck INTEGER
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        skill_name TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS character_skills (
        character_id INTEGER,
        skill_id INTEGER,
        PRIMARY KEY (character_id, skill_id),
        FOREIGN KEY (character_id) REFERENCES characters (character_id),
        FOREIGN KEY (skill_id) REFERENCES skills (skill_id)
    );
    ''')
    
    conn.commit()
    conn.close()

def add_characters(num_characters=10):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for _ in range(num_characters):
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        strength = fake.random_int(min=3, max=18)
        agility = fake.random_int(min=3, max=18)
        endurance = fake.random_int(min=3, max=18)
        intelligence = fake.random_int(min=3, max=18)
        luck = fake.random_int(min=3, max=18)

        cursor.execute('''INSERT INTO characters (first_name, last_name, job, town, strength, agility, endurance, intelligence, luck)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (first_name, last_name, job, town, strength, agility, endurance, intelligence, luck))

    conn.commit()
    conn.close()

def add_skills():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Добавляем навыки
    skills = [
        'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар',
        'Кислотный взгляд', 'Тайный побег', 'Огненный заряд',
        'Вихревой удар', 'Защитный барьер', 'Лечебное заклинание', 'Ядовитый укол'
    ]

    for skill in skills:
        cursor.execute("INSERT INTO skills (skill_name) VALUES (?)", (skill,))

    conn.commit()
    conn.close()

def main():
    create_tables()
    add_skills()
    add_characters(10)  # Добавляем 10 персонажей

if __name__ == '__main__':
    main()
