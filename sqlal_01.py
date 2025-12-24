'''

Getting started with SQLAlchemy     

Komal, December 2025

This series of programs are step by step guide to using SQLAlchemy for database access.

https://www.sqlalchemy.org/

In this code we use the SQL Alchemy database engine to create a db object in memory to run a simple SELECT statement.

'''

# imports
from sqlalchemy import create_engine, text


# create DB connection engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)    # keep echo on for debugging messages

# execute SQL 
with engine.connect() as conn:      # create a connection to the database (in memory)
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

