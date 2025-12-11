from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)       # NB : echo off


''' In this example, pass parameters to the SELECT command '''

# create table in memory and insert data (many values)
with engine.begin() as conn:    
    conn.execute(text("CREATE TABLE myTable (x int, y int)"))
    conn.execute(
        text("INSERT INTO myTable (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}, {"x": 3, "y": 2}, {"x": 4, "y": 4}],
    )
    

# execute SELECT on myTable, with WHERE clause
    result = conn.execute(text("select * from myTable where y >= :val "), {"val": 2})
    print("\nSelect with WHERE y >= 2")
    for row in result:      # result comes back as a list
        print(f"x: {row.x} \t y: {row.y}")


