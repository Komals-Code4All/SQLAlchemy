'''
DATABASE REFLECTION 
------------------- 

This program accesses a local MySQL server and connects to the SAKILA database.
Information about the database's tables and their columns is then retrieved. 

This could be done using SQL connectors and SQL statement 'SHOW TABLES'. 
However, here it is done in an OOP style

'''

from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine


# declare MetaData object
metadata_obj = MetaData()

# create DB engine connection. Userid='root', pasword='sqluser'
engine = create_engine("mysql+pymysql://root:sqluser@localhost/sakila", echo=False)

# get list of tables in the database ( ==> table reflection)
metadata_obj.reflect(bind=engine)
myTables = metadata_obj.tables

for t in myTables:

    # create / map Sakila table 't' into a table object
    table = Table(t, metadata_obj, autoload_with=engine)

    print(f"\nTABLE: {table.description.upper()}")
    # 'col' is short name for 'column'
    for col in table.columns:
        print(f"{col.name} \t\t {col.type} \t\t ", end="")  # end='' stops going on to a new line
        print("Primary Key") if col.primary_key == True else print()



#---------------------------------------------------------------------------------------------------
# Example below shows how you can access one known table at a time, and map that table as an object

# # map Sakila 'ACTOR' table into actor_table object
# actor_table = Table("actor", metadata_obj, autoload_with=engine)

# print(f"\nTABLE: {actor_table.description}")
# # 'col' is short name for 'column'
# for c in actor_table.columns:
#     print(f"{c.table} \t\t {c.name} \t\t {c.type} \t\t primary_key={c.primary_key}" )

#---------------------------------------------------------------------------------------------------

''' Next we look at how to run a query on a Sakila table'''

