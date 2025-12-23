# SQL Alchamy Tutorial code

Step-by-step code demonstrating SQLAlchemy

## Starting core concepts

https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial

<code> pip install SQLalchemy </code>

greenlet==3.3.0
SQLAlchemy==2.0.45
typing_extensions==4.15.0

In these first few examples there is no SQL server. SQLAlchemy creates a temp SQL database in memory. Data inserted into tables is lost when the program ends.

| Program  | Demonstrating                                    |
| -------- | ------------------------------------------------ |
| sqlal_01 | Hello World in SQL format                        |
| sqlal_02 | Create a table in memory and add some data to it |
| sqlal_03 | Define an SQL TRANSACTION and allow autocommit   |
| sqlal_04 | pass parameters to the SELECT ... WHERE command  |
| sqlal_05 | beginning OOP style coding                       |

## Working with Database Metadata (ORM)

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html

In this section we look at how to map SQL terminology, i.e. database, table and column, to SQLAlchemy's Python ORM / OOP style terminology.

The main import is a MetaData object, within which all tables will be defined and created.

<code> from sqlalchemy import MetaData
metadata_obj = MetaData() </code>

| Program  | Demonstrating                         |
| -------- | ------------------------------------- |
| sqlal_11 | Define SQL table as an ORM oject      |
| sqlal_12 | Define 2nd SQL table with foreign key |
| sqlal_13 | Create the database and add data      |

## Working with Database Classes and OOP

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#using-orm-declarative-forms-to-define-table-metadata

Finally, we use Python classes to define our database, whilst still using the underlying MetaData base models.

<code> from sqlalchemy.orm import DeclarativeBase </code>

| Program  | Demonstrating                    |
| -------- | -------------------------------- |
| sqlal_21 | Define SQL table as an OOP oject |
| sqlal_22 |                                  |
| sqlal_23 |                                  |

## Misc Programs

| Program           | Demonstrating                                    |
| ----------------- | ------------------------------------------------ |
| sqlal_99_mysql.py | Connecting to local installation of MySQL/Sakila |
