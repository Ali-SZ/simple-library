import sqlite3
import PyQt5

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
    
def databaseConnection():
    conn = sqlite3.connect(DATABASE_LOCATION)
    return conn

def addNewMember(name, phone, email, address):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(ADD_MEMBER.format(1, name, phone, email, address))
    conn.commit()
    conn.close()

def deleteMember(id):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(DELETE_MEMBER.format(id))
    conn.commit()
    conn.close()

def addNewBook(name, author, publisher, year, quantity):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(ADD_BOOK.format(name, author, publisher, year, quantity))
    conn.commit()
    conn.close()
    
def deleteBook(id):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(DELETE_BOOK.format(id))
    conn.commit()
    conn.close()
