# This is for icons, sql commands and etc.

# ********************* Sizes *********************
OPEN_MENU_WIDTH = int(175)
CLOSED_MENU_WIDTH = int(40)

# ********************* Database *********************
DATABASE_LOCATION = "Resources/database.db"
MEMBERS_HEADERS_LIST = ['Name', 'Phone', 'Email', 'Address']
BOOKS_HEADERS_LIST = ['Title', 'Author', 'Publisher', 'Year', 'Quantity']

# ********************* Icons *********************
ICONS_LOCATION = "Resources/Icons/"
MENU_ICON_LOCATION = ICONS_LOCATION + "menu.png"
MEMBERS_ICON_LOCATION = ICONS_LOCATION + "members.png"
BOOKS_ICON_LOCATION = ICONS_LOCATION + "books.png"
BORROWS_ICON_LOCATION = ICONS_LOCATION + "borrow.png"

# ********************* SQL Commands *********************
CREATE_MEMBERS_TABLE = "CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT, premission BIT);"
CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publisher TEXT, year INTEGER, quantity INTEGER);"
CREATE_BORROWS_TABLE = "CREATE TABLE IF NOT EXISTS borrows (id INTEGER PRIMARY KEY, member_id INTEGER, book_ids TEXT, borrow_date TEXT, return_date TEXT);"
SELECT_ALL_MEMBERS = "SELECT * FROM members"
SELECT_ALL_BOOKS = "SELECT * FROM books"
ADD_MEMBER = "INSERT INTO members(name, phone, email, address, premission) VALUES('{}', '{}', '{}', '{}', 1);"
DELETE_MEMBER = "DELETE FROM members WHERE id = {}"
EDIT_MEMBER = "UPDATE members SET name = '{}', phone = '{}', email = '{}', address = '{}' WHERE id = {}"
MEMBER_CLOSE_PERMISSION = "UPDATE members SET premission = 0 WHERE id = {}"
MEMBER_GIVE_PERMISSION = "UPDATE members SET premission = 1 WHERE id = {}"
ADD_BOOK = "INSERT INTO books (title, author, publisher, year, quantity) VALUES ('{}', '{}', '{}', '{}', '{}')"
DELETE_BOOK = "DELETE FROM books WHERE id = {}"
BOOK_LOWER_QUANTITY = "UPDATE books SET quantity = quantity - 1 WHERE id = {}"
BOOK_RAISE_QUANTITY = "UPDATE books SET quantity = quantity + 1 WHERE id = {}"
EDIT_BOOK = "UPDATE books SET title = '{}', author = '{}', publisher = '{}', year = '{}', quantity = '{}' WHERE id = {}"
ADD_NEW_BORROW = "INSERT INTO borrows (member_id, book_ids, borrow_date, return_date) VALUES ('{}', '{}', '{}', '{}')"
DELETE_BORROW = "DELETE FROM borrows WHERE id = {}"

