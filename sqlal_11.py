from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

'''

Define a user Table
    Table:      user_account
    columns:    id, name, full_name

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

# display database object definitions
print(user_table.c.name)
print(user_table.primary_key)
print(user_table.c.keys())
