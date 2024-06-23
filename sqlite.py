import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    genre TEXT
)
''')

connection.commit()

cursor.execute('DELETE FROM books')
connection.commit()

books = [
    (1, 'Lord of The Rings', 'J. R. R. Tolkien', 1954, 'Fantasy'),
    (2, '1984', 'George Orwell', 1949, 'Dystopian'),
    (3, 'The Hobbit', 'J. R. R. Tolkien', 1937, 'Fantasy'),
    (4, 'Fahrenheit 451', 'Ray Douglas Bradbury', 1953, 'Science fiction'),
    (5, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 1997, 'Fantasy')
]

cursor.executemany('''
INSERT INTO books (id, title, author, year, genre)
VALUES (?, ?, ?, ?, ?)
''', books)

connection.commit()

author = 'J. R. R. Tolkien'
cursor.execute('''
SELECT * FROM books WHERE author = ?
''', (author,))

results = cursor.fetchall()
for row in results:
    print(row)

new_year = 1952
book_id = 2
cursor.execute('''
UPDATE books SET year = ? WHERE id = ?
''', (new_year, book_id))

connection.commit()

book_id_delete = 4
cursor.execute('''
DELETE FROM books WHERE id = ?
''', (book_id_delete,))

connection.commit()

cursor.close()
connection.close()
