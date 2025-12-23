# SQL Alchamy Tutorial code

Step-by-step code demonstrating SQLAlchemy

https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial

<code> pip install SQLalchemy <code>


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
