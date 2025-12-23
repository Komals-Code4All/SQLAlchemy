
''' In this example, pass parameters to the SELECT command '''

from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)       # NB : echo off



# create table in memory and insert data (many values)
with engine.begin() as conn:    
    conn.execute(text("CREATE TABLE myTable (id int, fname str)"))
    conn.execute(
        text("INSERT INTO myTable (id, fname) VALUES (:id, :fname)"),
        [{"id": 1000, "fname": "Fred"}, 
         {"id": 1001, "fname": "Wilma"},
         {"id": 1002, "fname": "Barney"},
         {"id": 1003, "fname": "Betty"},
         {"id": 1004, "fname": "Peebles"},
         {"id": 1005, "fname": "Bambam"},],
    )    

# execute SELECT ... WHERE ... ORDER BY by fname
with engine.connect() as conn:
    result = conn.execute(
        text("select * from myTable where fname like :name order by fname"), {"name": "B%"})
    
    # Print the results
    print(f"\nName \t Id")
    print(20 * '-')
    for row in result:      # result comes back as a list
        print(f"{row.fname} \t {row.id}")
