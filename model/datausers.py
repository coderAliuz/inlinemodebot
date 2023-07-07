import sqlite3
connect=sqlite3.connect("data.db")
cursor=connect.cursor()

def check_users(chat_id):
    data=cursor.execute(f"SELECT id FROM users WHERE id={chat_id}")
    if data.fetchone() is None:
        return False #id mavjud bolmasa
    else:
        return True #id mavjud bolsa

# print(check_users(1122))

def user_add(chat_id,fullname,phone):
    cursor.execute(f"INSERT INTO users(id,fullname,phone) VALUES({chat_id},'{fullname}','{phone}')")
    connect.commit()

def data_edit_fullname(chat_id,fullname):
    cursor.execute(f"""UPDATE users SET fullname='{fullname}' WHERE id={chat_id}""")
    connect.commit()

def delete_users(chat_id):
    cursor.execute(f"DELETE FROM users WHERE id={chat_id}")
    connect.commit()

def count_users():
    number=cursor.execute("SELECT COUNT(*) FROM users")
    return number.fetchone()[0] #(10,)
# print(count_users())

def about_users(chat_id):
    info=cursor.execute(f"SELECT * FROM users WHERE id={chat_id}")
    return info.fetchone()

def get_chat_ids():
    ids=cursor.execute("SELECT id FROM users")
    return ids.fetchall()