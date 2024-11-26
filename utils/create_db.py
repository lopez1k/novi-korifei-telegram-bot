from sqlite3 import connect

class CreateDB():
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS spectacls (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, place TEXT, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, name TEXT, phone_number TEXT, admin INTEGER DEFAULT '0')")
    cur.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL, author_name TEXT, author_phone TEXT, title TEXT, status TEXT DEFAULT 'Відкрито')")
    conn.commit()
    conn.close()