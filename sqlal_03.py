from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


''' In this example, engine.begin starts a DB transaction 
    which will autocommit. So, no need to issue a conn.commit() [ it causes errors]
'''

# create table in memory and insert data.
with engine.begin() as conn:    
    conn.execute(text("CREATE TABLE myTable (x int, y int)"))
    conn.execute(
        text("INSERT INTO myTable (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.execute(
        text("INSERT INTO myTable (x, y) VALUES (:x, :y)"),
        [{"x": 3, "y": 2}, {"x": 4, "y": 4}],
    )
    #conn.commit()   # commit changes NO NEED FOR THIS



# execute SELECT on myTable , order by Y
    result = conn.execute(text("select * from myTable order by y"))
    print("\nDisplay using index values row[n]")
    for row in result:      # result comes back as a list
        print(f"x: {row[0]} \t y: {row[1]}")

# execute SELECT on myTable , order by Y
    result = conn.execute(text("select * from myTable order by y"))
    print("\nDisplay using attribute names row.x")
    for row in result:      # result comes back as a list
        print(f"y: {row.y} \t x: {row.x}")


