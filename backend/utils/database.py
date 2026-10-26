import psycopg2
from psycopg2 import extras
from psycopg2.extras import RealDictCursor
import os

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "cafe"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def execute_query(query, params=None, fetch=False):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute(query, params)
        
        if fetch:
            results = cursor.fetchall()
            conn.commit() 
            return [dict(row) for row in results]
        else:
            conn.commit()
            return cursor.rowcount
            
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Ошибка выполнения SQL: {e}")
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()