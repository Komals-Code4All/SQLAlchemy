''' 

Getting started with SQLAlchemy     

Komal, December 2025


In db terminology a TRANSACTION is a complete event, from beginning to end, that operates on a database, 
and may (C) change, (R) retrieve, (U) update or (D) delete data. [NB C.R.U.D.]

If the transaction completes normally then changes are COMMITed to the database.
If for any reason the transaction fails then changes that have been applied can be ROLLedBACK, i.e. not COMMITed.

In this example, engine.begin starts a db transaction which will autocommit. Issuing a conn.commit() will raise a runtime error.

Data table : myTable
(   id, integer, 
    fname, string
)

'''

# imports
from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Start DB Transaction 

# create table in memory and insert data.
with engine.begin() as conn:    
    conn.execute(text("CREATE TABLE myTable (id int, fname str)"))

    # Insert multiple rows of data in one execute using SQL's substitution method
    conn.execute(
        text("INSERT INTO myTable (id, fname) VALUES (:id, :fname)"),
        [{"id": 1000, "fname": "Fred"}, 
         {"id": 1001, "fname": "Wilma"},
         {"id": 1002, "fname": "Barney"},
         {"id": 1003, "fname": "Betty"},
         {"id": 1004, "fname": "Peebles"},
         {"id": 1005, "fname": "Bam Bam"},],
    )    

# assume normal end of db Transaction (Commit changes automatically)


''' 
    Transaction block ends when indentation ends, autocommit will occur here when INSERTs have been done
'''

'''
    So, we need to reconnect for SELECT commands
'''

# Open new DB connection to execute SELECT on myTable, order by first name
with engine.connect() as conn:
    result = conn.execute(text("select * from myTable order by fname"))
    print("\nDisplay using index values row[n]")
    for row in result:      # result comes back as a list
        print(f"id: {row[0]} \t fName: {row[1]}")     # using list indexing method


'''
    Reconnect for more SELECT commands
'''
# Open new DB connection to execute SELECT on myTable, order by first name
with engine.connect() as conn:
    result = conn.execute(text("select * from myTable order by fname"))
    print("\nDisplay using attribute names row.id")
    for row in result:      # result comes back as a list
        print(f"fName: {row.fname} \t id: {row.id}")  # using dictionary name

