import sqlite3

def foreign_key_on():
    conn = sqlite3.connect("users.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def creat_table(): 
    conn = foreign_key_on()
    cursor = conn.cursor()
    

#     cursor.execute("""
# DROP TABLE IF EXISTS orders;
#  """)
#     cursor.execute("""
# DROP TABLE IF EXISTS users;
#  """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
                   )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        produck_name TEXT NOT NULL,
        price INTEGER NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) 
            REFERENCES users(id)
            ON DELETE CASCADE
                    )
    """)
    
    conn.commit()
    conn.close()



def add_user(name,email):
    conn = foreign_key_on()
    cursor = conn.cursor()


    try:
        cursor.execute(
            "INSERT INTO users (name,email) VALUES (?,?)",
            (name,email)
        )
    except sqlite3.IntegrityError:
        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()
    return 1


def add_order(user_id,product_name,price):
    conn = foreign_key_on()
    cursor = conn.cursor()


    try:
        cursor.execute(
            "INSERT INTO orders (user_id,produck_name,price) VALUES (?,?,?)",
            (user_id,product_name,price)
        )
    except sqlite3.IntegrityError:
        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()
    return 1

def get_all_user_and_order():
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute("""
SELECT users.name, orders.produck_name,users.id,orders.price,orders.id
FROM users
LEFT JOIN orders ON orders.user_id = users.id
""")

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_order():
    conn = foreign_key_on()
    cursor = conn.cursor()


    cursor.execute("""
SELECT users.name,orders.produck_name,users.id,orders.price,orders.id
FROM users
INNER JOIN orders ON orders.user_id = users.id
""")

    rows = cursor.fetchall()
    conn.close()
    return rows



def get_users():
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    conn.close()
    return users


def delete_order(id):
    conn = foreign_key_on()
    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM orders WHERE id = ?",
        (id,)
    )
    
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows


def delete_user(id):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (id,)
        )
    
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows



def update_user(name,email,id:int):
    conn = foreign_key_on()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name = ?,email = ? WHERE id = ?",
        (name,email,id)
        )
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows
