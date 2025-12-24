'''

Getting started with SQLAlchemy     

Komal, December 2025

This example adds a 2nd table with a foreign key, connecting it to the 1st table.

Define a user table
    Table:      user_account
    columns:    id(PK), name, full_name


Define a user email_address table, with FK
    Table:      address
    columns:    id(PK), user_id(FK=user_account.name), email_address


'''

# imports
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey


# declare MetaData object
metadata_obj = MetaData()

# define table, user_account
user_table = Table("user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

# define user email address table
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


# display database object definitions
print('\nUser table')
print(f"Table columns: {user_table.c}") # 'c' is built-in 'column collection' object
print(f"Table Primary key details : {user_table.primary_key}") 
print(f"Table columns : {user_table.c.keys()}")


print('\nEmail addresses table')
print(f"Table columns: {address_table.c}") # 'c' is built-in 'column collection' object
print(f"Table Primary key details : {address_table.primary_key}") 
print(f"Table columns : {address_table.c.keys()}")

