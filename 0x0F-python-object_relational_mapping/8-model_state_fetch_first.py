#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(userName, passWord, dbName), pool_pre_ping=True)
    session = Session(engine)

    state = session.query(State).first()

    print(f"{state.id}: {state.name}")

    session.close()
