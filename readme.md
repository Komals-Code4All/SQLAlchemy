# Getting started with SQLAlchemy

## Komal, December 2025

This repo is a step-by-step guide to using Python and SQLAlchemy for database access.

Information is based on the documentation on the official website : https://www.sqlalchemy.org/

You will need an understanding of Python, OOP and SQL together with an idea on how relational databases work.

Early program examples start by accessing a virtual database, **SQLIte3**, held in memory. Therefore, you don't need to install anything database server on your devices.

Later examples will start using an locally installed database server, such as MySQL or PostGres. You can install either when we get to that section. Installation information is not provided here.

Install SQLAlchemy modules using <code> pip install SQLalchemy </code>. This should install the following latest versions of

    greenlet==3.3.0
    SQLAlchemy==2.0.45
    typing_extensions==4.15.0

## Section 01 : Starting core concepts

https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial

In these first few examples there is no SQL server. SQLAlchemy creates a temp SQL database in memory. Data inserted into database tables is lost when the program ends.

| Program  | Demonstrating                                    |
| -------- | ------------------------------------------------ |
| sqlal_01 | Hello World in SQL format                        |
| sqlal_02 | Create a table in memory and add some data to it |
| sqlal_03 | Define an SQL TRANSACTION and allow autocommit   |
| sqlal_04 | pass parameters to the SELECT ... WHERE command  |
| sqlal_05 | beginning OOP style coding                       |

## Section 02: Moving towards ORM Database Model

In this section we look at how to map SQL terminology, i.e. database, table and column, to SQLAlchemy's Python ORM / OOP style terminology.

Full explanations : https://docs.sqlalchemy.org/en/20/tutorial/metadata.html

The module to import gives a **MetaData** object, with which all tables will be defined and created.

<code>from SQLalchemy import MetaData </code>

<code>metadata_obj = MetaData() </code>

| Program  | Demonstrating                         |
| -------- | ------------------------------------- |
| sqlal_11 | Define SQL table as an ORM object     |
| sqlal_12 | Define 2nd SQL table with foreign key |
| sqlal_13 | Create the database and add data      |

## Section 03: Working with Database Classes and OOP

Here we use Python classes to define our database, whilst still using the underlying MetaData base models.

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#using-orm-declarative-forms-to-define-table-metadata

<code> from SQLAlchemy.orm import DeclarativeBase </code>

| Program  | Demonstrating                                 |
| -------- | --------------------------------------------- |
| sqlal_21 | Define SQL table as an **OOP** object         |
| sqlal_22 | Issuing INSERT statement in SQLALchemy format |

## Misc Programs

Some worked examples showing various hints and tips

The examples use

- MySQL with the free-to-install **Sakila** movie database
- PostGresSQL with the free-to-install **Chinook** music database

| Program              | Demonstrating                                                          |
| -------------------- | ---------------------------------------------------------------------- |
| installTest.py       | Check SQLAlchemy version                                               |
|                      |                                                                        |
| sqlal_99_mysql_01.py | Connect to a local MySQL server, and retrieve table definitions        |
| sqlal_99_mysql_02.py | Connect to a local MySQL server, run SQL SELECT query on existing data |
|                      |                                                                        |
| sqlal_99_postgres.py | Connecting to local Postgres, Chinook database                         |
