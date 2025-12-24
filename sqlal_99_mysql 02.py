'''

Example of connecting to local MySQL with SAKILA database installed

    pip install SQLAlchemy


Open the MySQL Dashboard and you will see this program affecting the Network Status, 
in the data sent/recd graph

Other tables in Saklia you could try accessing: 
    actor, actor_info, address, city, customer, film, film_actor, staff, rental, store

'''

from sqlalchemy import create_engine, text


# create DB engine object. User id='root', pasword='sqluser'
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

