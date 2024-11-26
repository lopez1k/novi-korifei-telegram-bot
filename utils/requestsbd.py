from sqlite3 import connect

async def exists_user(uid):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE uid = ?", (uid,))
    res = cur.fetchone()
    conn.close()
    return res

async def create_user(uid, full_name, number_phone):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (uid, name, phone_number) VALUES (?, ?, ?)", (uid, full_name, number_phone))
    conn.commit()
    conn.close()

async def create_spect_db(name, desc, place, date):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO spectacls (name, desc, place, date) VALUES (?, ?, ?, ?)", (name, desc, place, date))
    conn.commit()
    conn.close()

async def check_admin(uid):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT admin FROM users WHERE uid = ?", (uid,))
    res = cur.fetchone()[0]
    conn.close()
    return res

async def get_all_users():
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    res = cur.fetchall()
    conn.close()
    return res

async def get_spect():
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM spectacls")
    res = cur.fetchall()
    conn.close()
    return res
    
async def get_cur_spect(id):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM spectacls WHERE id = ?", (id,))
    res = cur.fetchone()
    conn.close()
    return res
    
async def get_sheets():
    cur = connect("data/main.db").cursor()
    cur.execute("SELECT name, phone_number FROM users")
    result = cur.fetchall()
    return result

async def get_tickets():
    conn = connect('data/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    res = cur.fetchall()
    conn.close()
    return res


async def create_ticket(uid, title):
    conn = connect('data/main.db')
    cur = conn.cursor()
    cur.execute("SELECT name, phone_number FROM users WHERE uid = ?", (uid,))
    res = cur.fetchone()
    cur.execute("INSERT INTO tickets (author_id, author_name, author_phone, title) VALUES (?, ?, ?, ?)", (uid, res[0], res[1], title))
    conn.commit()
    conn.close()
    return res

async def get_need_ticket(id: int):
    conn = connect('data/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE id = ?", (id,))
    res = cur.fetchone()
    conn.close()
    return res

async def delete_ticket(id: int):
    conn = connect('data/main.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM tickets WHERE id = ?", (id,))
    conn.commit()
    conn.close()