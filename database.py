import sqlite3
conn_db = sqlite3.connect("librarydb.db")
conn_db.execute('''
               CREATE TABLE library(
                book_name VARCHAR(50) PRIMARY KEY,
                book_author VARCHAR(60),
                book_price INT(5)
               )     
            ''')
conn_db.close()

