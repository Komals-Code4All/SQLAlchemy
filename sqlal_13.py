from sqlalchemy import create_engine

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, text

'''

Create tables and add data

'''

# declare MetaData object
metadata_obj = MetaData()

# define table, user_account
user_table = Table("user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

# define user address table
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# create database tables
metadata_obj.create_all(engine)

'''  Look at the terminal output, it should have SQL commands

    CREATE TABLE user_account (
        id INTEGER NOT NULL,
        name VARCHAR(30),
        fullname VARCHAR,
        PRIMARY KEY (id)
)


'''

with engine.begin() as conn:    
    #conn.execute(text("CREATE TABLE myTable (id int, fname str)"))

    # Insert multiple rows, in one execute, using SQL's substituton method
    conn.execute(
        text("INSERT INTO user_account (id, name, fullname) VALUES (:id, :name, :fullname)"),
        [{"id": 1000, "name": "Fred", "fullname":"Mr Fred Flinstone"}, 
         {"id": 1001, "name": "Wilma", "fullname":"Mrs Wilma Flintstone"},
         {"id": 1002, "name": "Barney", "fullname":"Mr Barney Rubble"},
         {"id": 1003, "name": "Betty", "fullname":"Mrs Betty Rubble"},
         {"id": 1004, "name": "Peebles", "fullname":"Miss Pebbles Flintstone"},
         {"id": 1005, "name": "Bambam", "fullname":"Master Bambam Rubble"},],
    )    

# Open new DB connecion to execute SELECT
with engine.connect() as conn:
    result = conn.execute(text("select * from user_account order by id"))
    print("\n")
    for row in result: 
        print(f"{row.id} {row.name} \t{row.fullname} ")    # using dictionary name

