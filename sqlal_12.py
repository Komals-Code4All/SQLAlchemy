from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey

'''
Define a second table
---------------------
NB: we don't actually create tables or add data in this example


Define a user table
    Table:      user_account
    columns:    id(PK), name, full_name


Define a user email_address table
    Table:      address
    columns:    id(PK), user_id(FK=user_account.name), email_address

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


# display database object definitions
print('User table')
print(user_table.c.name)
print(user_table.primary_key)
print(user_table.c.keys())

print('Email adresses table')
print(address_table.c.id)
print(address_table.primary_key)
print(address_table.c.keys())
