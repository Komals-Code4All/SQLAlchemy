from sqlalchemy import create_engine
from sqlalchemy import text

# create DB engine object
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# execute SQL 
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())


