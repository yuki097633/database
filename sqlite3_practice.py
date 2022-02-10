import sqlite3

# コネクションオブジェクトを返す
con = sqlite3.connect("sample.db")
# cursor作成　おまじない
cursor = con.cursor()

create_user_table_query = """
create table if not exists User(
    UserId integer primary key not null,
    Name text default "anonymous",
    Email text not null,
    Age integer check(Age > 0)
)
"""

# テーブル作成
cursor.execute(create_user_table_query)

insert_user_query = """
insert into User values (1, "john", "john@gmail.com", 30);
insert into User values (2, "emily", "emily@gmail.com", 30);
insert into User values (3, "taro", "taro@gmail.com", 30);
"""

# レコード作成
cursor.executescript(insert_user_query)
# コミットが必要
con.commit()
