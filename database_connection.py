import sqlite3

from Resources_init import *

def isDatabaseExist():
    try:
        conn = sqlite3.connect(DATABASE_LOCATION)
        conn.close()
        return True
    except:
        return False

def createDatabase():
    conn = sqlite3.connect(DATABASE_LOCATION)
    c = conn.cursor()
    c.execute(CREATE_MEMBERS_TABLE)
    c.execute(CREATE_BOOKS_TABLE)
    conn.commit()
    conn.close()