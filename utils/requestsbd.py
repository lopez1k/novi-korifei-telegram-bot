from sqlite3 import connect
import sqlite3
from datetime import datetime
import qrcode
import os


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

async def create_spect_db(name, desc, place, date, price, photo):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO spectacls (name, desc, place, date, price, photo_ticket) VALUES (?, ?, ?, ?, ?, ?)", (name, desc, place, date, int(price), photo))
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

async def get_suggestions():
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestions")
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
    
async def get_cur_spect_name(name):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM spectacls WHERE name  = ?", (name,))
    res = cur.fetchone()
    conn.close()
    return res
    

async def get_user_tickets(uid):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ticket_spect WHERE owner_id  = ?", (uid,))
    res = cur.fetchall()
    conn.close()
    return res
    

async def create_request_ticket(idspect, uid):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO requ_ticket(uid, spect_id) VALUES (?, ?)", (uid, idspect))
    conn.commit()
    res = cur.lastrowid
    conn.close()
    return res
    


async def get_cur_spect_price(price, uid):
    conn = connect("data/main.db")
    cur = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        cur.execute("SELECT * FROM spectacls WHERE price = ?", (price,))
        spect = cur.fetchone()
        cur.execute("SELECT * FROM users WHERE uid = ?", (uid,))
        user = cur.fetchone()
        cur.execute("INSERT INTO ticket_spect (owner_id, owner_name, owner_phone, spect, date, purchase_date) VALUES (?, ?, ?, ?, ?, ?)", (user[1], user[2], user[3], spect[1], spect[4], datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        conn.commit()
        img = qrcode.make(f'https://t.me/new_korifei_bot?start={user[1]}')
        type(img)
        img.save(f"{uid}.png")
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()



async def create_ticketss(spect_id, uid, moder):
    conn = connect("data/main.db")
    cur = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        cur.execute("SELECT * FROM requ_ticket WHERE id = ?", (spect_id,))
        requ_id = cur.fetchone()
        cur.execute("SELECT * FROM spectacls WHERE id = ?", (requ_id[2],))
        spect = cur.fetchone()
        cur.execute("SELECT * FROM users WHERE uid = ?", (uid,))
        user = cur.fetchone()
        print(user)
        print(spect)
        cur.execute("INSERT INTO ticket_spect (owner_id, owner_name, owner_phone, spect, date, purchase_date, accept_by) VALUES (?, ?, ?, ?, ?, ?, ?)", (user[1], user[2], user[3], spect[1], spect[4], datetime.now().strftime('%d-%m-%Y %H:%M:%S'), moder))
        cur.execute("DELETE FROM requ_ticket WHERE id = ?", (spect_id,))
        conn.commit()
        img = qrcode.make(f'https://t.me/new_korifei_bot?start={user[1]}')
        type(img)
        img.save(f"./{user[1]}.png")
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

async def getiser(id):
    conn = connect("data/main.db")
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM requ_ticket WHERE id = ?", (id,))
        uid = cur.fetchone()
        cur.execute("SELECT * FROM users WHERE uid = ?", (uid[1],))
        udata = cur.fetchone()
        return udata

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

async def insert_feedback(uid, text, spect):
    conn = connect("data/main.db")
    cur = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        cur.execute("SELECT name, phone_number FROM users WHERE uid = ?", (uid,))
        user = cur.fetchone()
        cur.execute("INSERT INTO feedback (author_id, author_name, author_phone, feedback, spect, date) VALUES (?, ?, ?, ?, ?, ?)", (uid, user[0], user[1], text, spect,  datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()



async def insert_suggestion(uid, text):
    conn = connect("data/main.db")
    cur = conn.cursor()
    try:
        conn.execute('BEGIN TRANSACTION')
        cur.execute("SELECT name, phone_number FROM users WHERE uid = ?", (uid,))
        user = cur.fetchone()
        cur.execute("INSERT INTO suggestions (author_id, author_name, author_phone, suggestion, date) VALUES (?, ?, ?, ?, ?)", (uid, user[0], user[1], text,  datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()









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