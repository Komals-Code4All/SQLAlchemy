'''

Getting started with SQLAlchemy     

Komal, December 2025

This program accesses a local MySQL server and connects to the SAKILA database. A SELECT statement is executed to get data.

Open your MySQL Workbench and look at the Dashboard. 
Every time this program is run you should see the Network Status graph show data being sent / rec'd.


'''

from sqlalchemy import create_engine, text


# create DB engine object. User id='root', password='sqluser'
engine = create_engine("mysql+pymysql://root:sqluser@localhost/sakila", echo=False)

# connect to Sakila and run query
with engine.connect() as conn:
    
    # execute SELECT on actor table
    result = conn.execute(text("select * from actor limit 10")) # limit to 10 rows
    for row in result:      # result comes back as a list
        print(f"{row.actor_id}, \t{row.first_name}, \t{row.last_name}")


    # execute SELECT on film table 
    result = conn.execute(text("select * from film limit 10"))
    for row in result:      # result comes back as a list
        print(f"{row.title}, \t({row.release_year}), \t{row.rating}, \t{row.description}" )


''' Next, we look at CRUD operations on the database '''
