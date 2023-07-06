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