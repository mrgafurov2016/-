import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname="hotel_db",
        user="hotel_user",
        password="hotel_password",
        host="localhost",  # или 'db' если в Docker
        port="5432"
    )

def execute_query(query, params=None, fetch=False, many=False):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            if many:
                cur.executemany(query, params)
            else:
                cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            conn.commit()
