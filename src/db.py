import sqlite3

try:
    connection = sqlite3.connect('./database/data.db')
except Exception as ex:
    print(ex)