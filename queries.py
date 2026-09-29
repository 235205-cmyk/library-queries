import sqlite3
conn = sqlite3.connect("library.db")
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT, genre TEXT, price INTEGER, stock INTEGER);
INSERT INTO books VALUES
(1,'Data Science Basics','Tech',1450,10),
(2,'Clean Code','Tech',1200,7),
(3,'The Silent Patient','Fiction',1350,2),
(4,'Atomic Habits','Self-Help',900,15),
(5,'1984','Fiction',700,4),
(6,'Python Crash Course','Tech',950,9),
(7,'Sapiens','History',800,6),
(8,'The Alchemist','Fiction',600,20);
""")
conn.commit()

print("Books above Rs.1000 (sorted):")
for r in cur.execute("SELECT title, price FROM books WHERE price > 1000 ORDER BY price DESC"):
    print(r)

print("\nWith alias:")
for r in cur.execute("SELECT title AS book_title, price FROM books"):
    print(r)

print("\nLow-stock Fiction books:")
for r in cur.execute("SELECT title, genre, price, stock FROM books WHERE genre='Fiction' AND stock < 5"):
    print(r)
conn.close()