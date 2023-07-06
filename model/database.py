import sqlite3
connect=sqlite3.connect("data.db")
cursor=connect.cursor()
from pprint import pprint
def CreataTable(table:str,colums:str):
    try:
        cursor.execute(f"CREATE TABLE {table}{colums}")
        connect.commit()
    except sqlite3.OperationalError:
        print("Bunday jadval mavjud")

# CreataTable("test2",'("id" INTEGER,"question" TEXT,"answer" VARCHAR(30))')

def InsertTable(table:str,colums:str,values:str):
    cursor.execute(f"INSERT INTO {table}{colums} VALUES{values}")
    connect.commit()

# InsertTable("test2",'("question","answer")','("2*2=?","4")')

def DropTable(table:str):
    '''Jadvalni o'chirib yuboradi'''
    cursor.execute(f"DROP TABLE {table};")
    connect.commit()

# DropTable("test1")

def DeleteColums(table:str):
    """Jadval ichidagi ma'lumotlarni tozalab yuboradi"""
    cursor.execute(f"DELETE FROM {table}")
    connect.commit()

# DeleteColums("foods")

def DeleteColum(table:str,colum:str,value:str):
    """Jadval ichidagi aynan berilgan ustundagi ma'lumotni tozalaydi"""
    cursor.execute(f"DELETE FROM {table} WHERE {colum}={value}")
    connect.commit()

# DeleteColum("test2","id","4")
# DeleteColum("test2","question","'2*2=?'")

def SelectTableAll(table):
    data=cursor.execute(f"SELECT * FROM {table}")
    return data.fetchall()

# getdata=SelectTableAll("test2")
# pprint(getdata[1])
# pprint(getdata[1][0])

def SelectTableOne(table,colum,value):
    data=cursor.execute(f"SELECT * FROM {table} WHERE {colum}='{value}'")
    return data.fetchone()

# getdata=SelectTableOne("test2","id","12")
# print(getdata)

def SelectTableColum(table,colum):
    data=cursor.execute(f"SELECT {colum} FROM {table}")
    return data.fetchall()

def UpdateTableALL(table,colum,volue):
    cursor.execute(f"UPDATE {table} SET {colum}={volue}")
    connect.commit()

# UpdateTableALL("test2","answer","'Yangi javob'")

# print(SelectTableColum("test2","answer"))

def UpdateTableOne(table,colum,volue,row,row_volue):
    cursor.execute(f"UPDATE {table} SET {colum}={volue} WHERE {row}={row_volue}")
    connect.commit()

UpdateTableOne("test2","answer","'togri javob'","id","12")
print(SelectTableColum("test2","answer"))