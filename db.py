import sqlite3



def creat_table(): 
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

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
        FOREIGN KEY (user_id) REFERENCES users(id)
                    )
    """)
    
    conn.commit()
    conn.close()



def add_user(name,email):
    conn = sqlite3.connect("users.db")
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



def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    conn.close()
    return users



def delete_user(id):
    conn = sqlite3.connect("users.db")
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
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name = ?,email = ? WHERE id = ?",
        (name,email,id)
        )
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows
