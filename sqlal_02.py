from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# create table in memory and insert data.
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE myTable (x int, y int)"))
    conn.execute(
        text("INSERT INTO myTable (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.execute(
        text("INSERT INTO myTable (x, y) VALUES (:x, :y)"),
        [{"x": 3, "y": 2}, {"x": 4, "y": 4}],
    )
    conn.commit()   # commit changes 

# execute SELECT on myTable 
    result = conn.execute(text("select * from myTable"))
    for row in result:      # result comes back as a list
        print(row)
