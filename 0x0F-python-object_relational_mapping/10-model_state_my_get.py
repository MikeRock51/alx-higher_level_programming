#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]
    reqState = argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{userName}:{passWord}@localhost/{dbName}',
        pool_pre_ping=True)

    session = Session(engine)
    states = session.query(State).filter(State.name == reqState).all()

    found = False

    for state in states:
        if reqState == state.name:
            print(state.id)
            found = True
            break
    if found is False:
        print("Not found")

    session.close()
