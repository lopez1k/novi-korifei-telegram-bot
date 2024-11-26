from sqlite3 import connect

class CreateDB():
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS spectacls (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, place TEXT, date TEXT, price INTEGER, photo_ticket TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, name TEXT, phone_number TEXT, admin INTEGER DEFAULT '0')")
    cur.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL, author_name TEXT, author_phone TEXT, title TEXT, status TEXT DEFAULT 'Відкрито')")
    cur.execute("CREATE TABLE IF NOT EXISTS ticket_spect (id INTEGER PRIMARY KEY, owner_id INTEGER NOT NULL, owner_name TEXT, owner_phone TEXT, spect TEXT, date TEXT, purchase_date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL, author_name TEXT, author_phone TEXT, feedback TEXT, spect TEXT, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS suggestions (id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL, author_name TEXT, author_phone TEXT, suggestion TEXT, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS requ_ticket (id INTEGER PRIMARY KEY, uid INTEGER, spect_id INTEGER)")
    conn.close()