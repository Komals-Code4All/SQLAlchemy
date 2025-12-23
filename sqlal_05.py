
''' 
    SQLAlchamy code can be written using a CORE or ORM style approach

    Core - basic standard appraoch to coding
    ORM  - Object Relation Mapping approach

    This example introduces ORM with the idea of a DB connection SESSION

'''

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session          # NB: extra import


# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False) 

# create table in memory and insert data (many values)
with Session(engine) as sesh:    
    sesh.execute(text("CREATE TABLE myTable (id int, fname str)"))
    sesh.execute(
        text("INSERT INTO myTable (id, fname) VALUES (:id, :fname)"),
        [{"id": 1000, "fname": "Fred"}, 
         {"id": 1001, "fname": "Wilma"},
         {"id": 1002, "fname": "Barney"},
         {"id": 1003, "fname": "Betty"},
         {"id": 1004, "fname": "Peebles"},
         {"id": 1005, "fname": "Bambam"},],
    )    

    # NB: commit changes at end of Session, otherwises changes are not saved
    sesh.commit()   


# execute SELECT ... WHERE ... ORDER BY by fname
sqlQry = text("select * from myTable where fname like :name order by fname")

with Session(engine) as sesh:
    result = sesh.execute(sqlQry, {"name": "B%"})
    
    # Print the results
    print(f"\nName \t Id")
    print(20 * '-')
    for row in result:      # result comes back as a list
        print(f"{row.fname} \t {row.id}")


    result = sesh.execute(sqlQry, {"name": "%e%"})      # NB: different query
    # Print the results
    print(f"\nName \t Id")
    print(20 * '-')
    for row in result:      # result comes back as a list
        print(f"{row.fname} \t {row.id}")
