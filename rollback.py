import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()
create_history_query = """
create table if not exists history (
    Name text,
    Age integer
)
"""

cursor.execute(create_history_query)

target_name = input("Whose age do you want to update?")
new_age = input("Tell me new age: ")
update_user_query = "update User " \
               "set age = ? " \
               "where name = ? "
insert_history_query = "insert into History " \
                       "values (?, ?)"

try:
    cursor.execute(update_user_query, (new_age, target_name))
    cursor.execute(insert_history_query, (target_name, new_age))
except sqlite3.Error:
    print("sqlite3 error occurred")
    con.rollback()
else:
    con.commit()
