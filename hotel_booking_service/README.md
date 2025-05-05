# Hotel Booking Service

Простой сервис бронирования отелей на Django с использованием PostgreSQL и raw SQL-запросов (psycopg2).

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

```bash
git clone https://github.com/mrgafurov2016/hotel-booking-service.git
cd hotel-booking-service
python -m venv venv
venv\Scripts\activate    # или source venv/bin/activate на Linux/macOS
pip install -r requirements.txt
