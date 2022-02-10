import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# for row in cursor.execute("select * from User"):
#     print(row)

cursor.execute("select * from User")
# cursorはイテレータ
print(next(cursor))
# print(next(cursor))

# .fetchall() 現在のcursor以下全てをタプルのリストで返す
# print(cursor.fetchall())

# .fetchone() 現在のcursorのレコードををタプルで返す
print(cursor.fetchone())

