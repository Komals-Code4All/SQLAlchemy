'''

Getting started with SQLAlchemy     

Komal, December 2025


SQLAlchemy code can be written using a CORE or ORM style approach

    Core - basic standard approach to coding
    ORM  - Object Relation Mapping approach

This example introduces ORM with the idea of a db connection SESSION object, rather than TRANSACTION object.

'''

# imports
from sqlalchemy import create_engine, text
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
         {"id": 1005, "fname": "Bam Bam"},],
    )    

    # NB: commit changes at end of Session, otherwise changes are not saved
    sesh.commit()


# execute SELECT ... WHERE ... ORDER BY by fname
sqlQry = text("select * from myTable where fname like :name order by fname")

with Session(engine) as sesh:

    # query 1: name starts with letter 'B'
    result = sesh.execute(sqlQry, {"name": "B%"})
    
    # Print the results
    print(f"\nName \t Id")
    print(20 * '-')
    for row in result:      # result comes back as a list
        print(f"{row.fname} \t {row.id}")

    # query 2: name contains letter 'e' anywhere in the string
    result = sesh.execute(sqlQry, {"name": "%e%"}) 
    # Print the results
    print(f"\nName \t Id")
    print(20 * '-')
    for row in result:      # result comes back as a list
        print(f"{row.fname} \t {row.id}")
