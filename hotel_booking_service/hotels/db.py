import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect()

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
