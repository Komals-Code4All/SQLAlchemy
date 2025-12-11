
''' 
    In this example, engine.begin starts a DB transaction which will autocommit. 
    So, no need to issue a conn.commit() [ it causes errors]

'''

from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Start DB Transaction 
# create table in memory and insert data.
with engine.begin() as conn:    
    conn.execute(text("CREATE TABLE myTable (id int, fname str)"))

    # Insert multiple rows, in one execute, using SQL's substituton method
    conn.execute(
        text("INSERT INTO myTable (id, fname) VALUES (:id, :fname)"),
        [{"id": 1000, "fname": "Fred"}, 
         {"id": 1001, "fname": "Wilma"},
         {"id": 1002, "fname": "Barney"},
         {"id": 1003, "fname": "Betty"},
         {"id": 1004, "fname": "Peebles"},
         {"id": 1005, "fname": "Bambam"},],
    )    

# end of DB Transaction (Commit changes)


''' Transaction block ends when indentation ends 
    Autocommit will occur when INSERTs have been done
    start new connection for SELECT commands
'''

# Open new DB connecion to execute SELECT on myTable, order by first name
with engine.connect() as conn:
    result = conn.execute(text("select * from myTable order by fname"))
    print("\nDisplay using index values row[n]")
    for row in result:      # result comes back as a list
        print(f"id: {row[0]} \t fName: {row[1]}")       # using list indexing method


# Open new DB connecion to execute SELECT on myTable, order by first name
with engine.connect() as conn:
    result = conn.execute(text("select * from myTable order by fname"))
    print("\nDisplay using attribute names row.id")
    for row in result:      # result comes back as a list
        print(f"fName: {row.fname} \t id: {row.id}")    # using dictionary name

