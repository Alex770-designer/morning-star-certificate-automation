import sqlite3
from datetime import datetime


DATABASE = "morningstar.db"


def get_connection():

    return sqlite3.connect(DATABASE)



def create_tables():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        grade TEXT,

        folder_id TEXT UNIQUE,

        certificate_id TEXT,

        status TEXT,

        created_date TEXT

    )
    """)


    conn.commit()
    conn.close()



if __name__ == "__main__":

    create_tables()

    print("Database created successfully!")