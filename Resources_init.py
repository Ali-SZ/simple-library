# This is for icons, sql commands and etc.

# ********************* Sizes *********************
OPEN_MENU_WIDTH = 175
CLOSED_MENU_WIDTH = 40

# ********************* Database *********************
DATABASE_LOCATION = "Resources/database.db"

# ********************* Icons *********************
ICONS_LOCATION = "Resources/Icons/"
MENU_ICON_LOCATION = ICONS_LOCATION + "menu.png"
MEMBERS_ICON_LOCATION = ICONS_LOCATION + "members.png"
BOOKS_ICON_LOCATION = ICONS_LOCATION + "books.png"
BORROWS_ICON_LOCATION = ICONS_LOCATION + "borrow.png"
SETTING_ICON_LOCATION = ICONS_LOCATION + "setting.png"

# ********************* SQL Commands *********************
CREATE_MEMBERS_TABLE = "CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)"
CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, name TEXT, author TEXT, publisher TEXT, year INTEGER, quantity INTEGER)"
