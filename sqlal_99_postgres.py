'''
Example of connecting to local PostGres installation to access the Chinook database

    pip install SQLAlchemy
    pip install psycopg2

'''

# imports
from sqlalchemy import create_engine, text

# create DB engine object. User id='postgres', password='sqluser', connecting to chinook database
engine = create_engine("postgresql+psycopg2://postgres:sqluser@localhost:5432/chinook", echo=True)

# connect to Chinook and run query
with engine.connect() as conn:
    
    # execute SELECT 
    result = conn.execute(text("select * from album order by title"))
    for row in result:      # result comes back as a list
        print(f"{row.album_id}, \t{row.title} ")


    # execute SELECT 
    result = conn.execute(text("select * from artist order by name "))
    for row in result:      # result comes back as a list
        print(f"{row.artist_id}, \t({row.name})" )

