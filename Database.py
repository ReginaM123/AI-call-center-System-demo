import sqlite3

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    phone TEXT,
    last_issue TEXT
)
""")

conn.commit()
