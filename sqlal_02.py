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

    conn.commit()   # commit changes 

# execute SELECT on myTable 
    result = conn.execute(text("select * from myTable"))
    for row in result:      # result comes back as a list
        print(row)
