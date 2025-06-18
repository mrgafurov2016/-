# Hotel Booking Service

Простой сервис бронирования номеров в отелях с HTTP JSON API, реализованный на Django и PostgreSQL с использованием SQL.

## Функции:
- Просмотр списка комнат
- Добавление и удаление бронирований
- Проверка занятости комнат

## Стек технологий:
- Python 3.13
- Django
- PostgreSQL
- psycopg2
- DRF
- poetry
- docker
- docker compose
- pytest

## Установка:

1. **Клонируй репозиторий:**

 git clone <URL репозитория>
 cd <название проекта>

2. **Создай и активируй виртуальное окружение (Windows):**

python -m venv .venv
.venv\Scripts\activate

**(или Linux/macOS):**

python3 -m venv .venv
source .venv/bin/activate

3. **Установи зависимости**

pip install -r requirements.txt

4. **Применить миграции:**

python manage.py migrate

5. **Запусти сервер**

python manage.py runserver

По умолчанию сервер доступен по адресу http://127.0.0.1:8000.

**ЭНДПОИНТЫ**

1. **Список комнат**

curl -X GET "http://127.0.0.1:8000/rooms/list"

2. **Создание комнаты**

curl -X POST -H "Content-Type: application/json" \ -d "{\"description\":\"Просторный люкс\", \"price\":3000}" \ http://127.0.0.1:8000/rooms/create

3. **Удаление комнаты**

curl -X DELETE "http://127.0.0.1:8000/rooms/delete?room_id=1"

4. **Создание бронирования**

curl -X POST -H "Content-Type: application/json" \ -d "{\"room_id\":1, \"date_start\":\"2025-05-30\", \"date_end\":\"2025-06-01\"}" \ http://127.0.0.1:8000/bookings/create

5. **Удаление бронирования**

curl -X DELETE "http://127.0.0.1:8000/bookings/delete?booking_id=1"

6. **Список бронирования для комнаты**

curl -X GET "http://127.0.0.1:8000/bookings/list?room_id=1"
