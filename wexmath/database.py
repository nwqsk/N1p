import sys
import sqlite3

import timer

# Ошибки
error = "[!] Ошибка БД | "
connectionError = error + "Невозможно подключиться к базе данных"

def quit():
    sys.exit()

def connect():
    try:
        return sqlite3.connect('users.db')
    except:
        print(connectionError)
        quit() 

def create():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(id STRING, username STRING, firstname STRING, lastname STRING, task STRING, points INTEGER, startTime INTEGER)""")
    connection.commit()

def add(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        cursor.execute("INSERT INTO login_id VALUES(?,?,?,?,?,?,?);", [msg.from_user.id , msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, '-', 0, timer.current()])
        connection.commit()
        return True
    else:
        connection.commit()
        return False

def remove(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        cursor.execute(f"DELETE FROM login_id WHERE id = {msg.from_user.id}")
        connection.commit()
        return True

def get_task(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        n = cursor.execute(f"SELECT task FROM login_id WHERE id = {msg.from_user.id}").fetchall()[0]
        connection.commit()
        return str(n)[:-2][1:]
    
def set_task(msg, task):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        cursor.execute(f"UPDATE login_id SET task = '{task}' WHERE id = {msg.from_user.id}")
        connection.commit()
        return True
    
def get_points(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        n = cursor.execute(f"SELECT points FROM login_id WHERE id = {msg.from_user.id}").fetchall()[0]
        connection.commit()
        return str(n)[:-2][1:]
    
def add_point(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        cursor.execute(f"UPDATE login_id SET points = '{str(int(str(get_points(msg))) + 1)}' WHERE id = {msg.from_user.id}")
        connection.commit()
        return True
    
def set_time(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        cursor.execute(f"UPDATE login_id SET startTime = '{timer.current()}' WHERE id = {msg.from_user.id}")
        connection.commit()
        return True
    
def get_time(msg):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM login_id WHERE id = {msg.from_user.id}")
    data = cursor.fetchone()

    if data is None:
        connection.commit()
        return False
    else:
        n = cursor.execute(f"SELECT startTime FROM login_id WHERE id = {msg.from_user.id}").fetchall()[0]
        connection.commit()
        return float(str(n)[:-2][1:])//1

def result_time(msg):
    return timer.count(get_time(msg))