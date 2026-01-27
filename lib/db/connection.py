import sqlite3

DB_NAME = "card_manager.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def get_cursor(conn):
    return conn.cursor()
