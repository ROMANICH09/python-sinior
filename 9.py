import sqlite3
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Подключение к существующей базе данных
conn = sqlite3.connect('db.sl3')
cursor = conn.cursor()

# Создаем таблицу, если её нет
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    temperature TEXT
)
''')
conn.commit()

# Функция для получения температуры с сайта
def get_temperature():
    url = "https://yandex.kz/pogoda/almaty?lat=43.273564&lon=76.914851"  # Ссылка на сайт с погодой для вашего города
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Извлекаем температуру
    temperature = soup.find("span", class_="temp__value temp__value_with-unit").text
    return temperature

# Получаем текущую температуру
try:
    temperature = get_temperature()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Вставляем данные в таблицу
    cursor.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (date_time, temperature))
    conn.commit()

    print(f"Данные успешно добавлены: {date_time}, {temperature}°C")
except Exception as e:
    print(f"Ошибка при получении данных: {e}")

# Закрываем соединение с базой данных
conn.close()
