'''

Getting started with SQLAlchemy     

Komal, December 2025

Again, create a db in memory and connect to it. 

Here, 
    execute an SQL CREATE TABLE statement, 
    add some data with two INSERT INTO statements and 
    then check results with SELECT

'''


# imports
from sqlalchemy import create_engine
from sqlalchemy import text


# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


# create table in memory and insert data.
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE myTable (id int, fname str)"))

    # insert 1st row
    conn.execute(
        text("INSERT INTO myTable (id, fname) VALUES (1000, 'Fred')" ), 
    )

    # insert 2nd row
    conn.execute(
        text("INSERT INTO myTable (id, fname) VALUES (1001, 'Wilma')" ), 
    )

    # commit all the changes (in memory) to the actual database tables
    conn.commit()   # commit changes 

# execute SELECT on myTable 
    result = conn.execute(text("select * from myTable"))
    for row in result:      # result comes back as a list
        print(row)
