

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import Table, Column, Integer, String, ForeignKey, text


'''

Define tables using OOP classes

'''

# use SQLAlchemy's DeclarativeBase class, as parent class for our tables
class Base(DeclarativeBase):
    pass

# define user_account table
class User(Base):
    __tablename__ = "user_account"

    # column mappings
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    # printing method format - 'repr' is a string representaton, built-in function
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"



# define address table
class Address(Base):
    __tablename__ = "address"

    # column mapping
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    # printing method format - 'repr' is a string representaton, built-in function
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# add data using OOP classes
fred = User(id=1000, name="Fred", fullname="Mr Fred Flinstone")
wilma = User(id=1001, name="Wilma", fullname="Mrs Wilma Flintstone")

barney = User(id=1002, name="Barney", fullname="Mr Barney Rubble")
betty = User(id=1003, name="Betty", fullname="Mrs Betty Rubble")

pebbles=User(id=1004, name="Peebles", fullname="Miss Pebbles Flintstone"),
bambam=User(id=1005, name="Bambam", fullname="Master Bambam Rubble")


# print objects
print(fred)
print(wilma)
print(barney)

''' NB: there is no database as such. Data is held in objects
    Next, we look at how to define a database using OOP notation '''