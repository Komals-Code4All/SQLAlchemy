'''

Getting started with SQLAlchemy     

Komal, December 2025

This example introduces using SQLAlchemy's MetaData ORM model to define a table and displays table information using OOP ideas.

Table:      user_account
columns:    id(PK), name, full_name

NB: No tables are actually created, nor is any data added. That will come later.

'''

# imports
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

# declare MetaData object
metadata_obj = MetaData()

# define user_account table
user_table = Table("user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

# display database object definitions

print(f"\nTable columns: {user_table.c}") # 'c' is built-in 'column collection' object

print(f"\nTable Primary key details : {user_table.primary_key}") 

print(f"\nTable columns : {user_table.c.keys()}")
