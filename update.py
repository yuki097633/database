import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

target_name = input("Whose age do you want to update?")
new_age = input("Tell me new age: ")
print(target_name, new_age)

# SQLインジェクションの脆弱性あり
# update_query = f"update User " \
#                f"set age = {new_age} " \
#                f"where name = '{target_name}'"
# cursor.executescript(update_query)

# SQLインジェクションの脆弱性を防ぐ プレースフォルダ
update_query = f"update User " \
               f"set age = ? " \
               f"where name = ? "

cursor.execute(update_query, (new_age, target_name))
con.commit()
