import sqlite3
import os

DB_NAME = "shop.db"

# remove existing db if exists so script is repeatable
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# -----------------------------
# Create tables
# -----------------------------
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    is_vip INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# -----------------------------
# Insert customers
# -----------------------------
customers = [
    (1, "Alice", 1),
    (2, "Bob", 0),
    (3, "Charlie", 1),
    (4, "Diana", 1),
    (5, "Eve", 0),
]

cursor.executemany("""
INSERT INTO customers (id, name, is_vip)
VALUES (?, ?, ?)
""", customers)

# -----------------------------
# Insert orders
# -----------------------------
orders = [
    (101, 1, 120.0, "failed", "2026-04-25 09:00:00"),
    (102, 1, 80.0, "success", "2026-04-25 10:00:00"),
    (103, 2, 50.0, "failed", "2026-04-25 11:00:00"),
    (104, 3, 200.0, "failed", "2026-04-25 12:00:00"),
    (105, 4, 90.0, "success", "2026-04-25 13:00:00"),
    (106, 3, 75.0, "failed", "2026-04-25 14:00:00"),
    (107, 4, 150.0, "failed", "2026-04-25 15:00:00"),
    (108, 5, 60.0, "success", "2026-04-25 16:00:00"),
]

cursor.executemany("""
INSERT INTO orders (id, customer_id, amount, status, created_at)
VALUES (?, ?, ?, ?, ?)
""", orders)

conn.commit()
conn.close()

print(f"{DB_NAME} created successfully.")
