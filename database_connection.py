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
    c.execute(CREATE_BORROWS_TABLE)
    conn.commit()
    conn.close()
    
def databaseConnection():
    conn = sqlite3.connect(DATABASE_LOCATION)
    return conn

def addNewMember(name, phone, email, address):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(ADD_MEMBER.format(name, phone, email, address))
    conn.commit()
    conn.close()

def deleteMember(id):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(DELETE_MEMBER.format(id))
    conn.commit()
    conn.close()
    
def editMember(id, name, phone, email, address):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(EDIT_MEMBER.format(name, phone, email, address, id))
    conn.commit()
    conn.close()

def addNewBook(title, author, publisher, year, quantity):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(ADD_BOOK.format(title, author, publisher, year, quantity))
    conn.commit()
    conn.close()
    
def deleteBook(id):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(DELETE_BOOK.format(id))
    conn.commit()
    conn.close()
    
def editBook(id, title, author, publisher, year, quantity):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(EDIT_BOOK.format(title, author, publisher, year, quantity, id))
    conn.commit()
    conn.close()
    
def borrowBook(member_id, book_ids, borrow_date, return_date):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(ADD_NEW_BORROW.format(member_id, book_ids, borrow_date, return_date))
    conn.commit()
    conn.close()
    
def returnBorrow(id):
    conn = databaseConnection()
    c = conn.cursor()
    c.execute(DELETE_BORROW.format(id))
    conn.commit()
    conn.close()
